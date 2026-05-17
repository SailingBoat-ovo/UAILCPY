import json
import os
import sys
import threading
import subprocess
from datetime import datetime

CONFIG_FILE = os.path.join(os.path.dirname(__file__), "ai_config.json")
HISTORY_FILE = os.path.join(os.path.dirname(__file__), "ai_history.json")

_OPENAI_AVAILABLE = False
try:
    import openai
    _OPENAI_AVAILABLE = True
except ImportError:
    _OPENAI_AVAILABLE = False


def ensure_openai():
    global _OPENAI_AVAILABLE
    if _OPENAI_AVAILABLE:
        return True
    try:
        import openai
        _OPENAI_AVAILABLE = True
        return True
    except ImportError:
        pass

    print("检测到缺少 openai 库，正在自动安装...")
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "openai", "-q"],
            capture_output=True, text=True, timeout=60
        )
        if result.returncode == 0:
            import openai
            _OPENAI_AVAILABLE = True
            print("openai 库安装成功！")
            return True
        else:
            print(f"pip 安装失败: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print("安装超时，请手动运行: pip install openai")
        return False
    except FileNotFoundError:
        print("未找到 pip，请手动安装 openai 库: pip install openai")
        return False
    except Exception as e:
        print(f"安装出错: {e}")
        return False

DEFAULT_CONFIG = {
    "api_key": "",
    "api_url": "https://api.deepseek.com",
    "model": "deepseek-v4-flash",
    "temperature": 0.7,
    "max_tokens": 2048,
    "system_prompt": "你是一位专业的编程教学AI老师。你的职责是：\n1. 用通俗易懂的语言解释编程概念\n2. 通过问答引导学生思考，而不是直接给答案\n3. 检查学生代码中的错误并给出修改建议\n4. 用比喻和类比帮助理解抽象概念\n5. 鼓励学生独立思考和解决问题\n6. 当学生遇到困难时，给出提示而不是完整解决方案\n\n请用中文回答，语气友好耐心。"
}

PROVIDER_PRESETS = {
    "DeepSeek": {
        "api_url": "https://api.deepseek.com",
        "model": "deepseek-coder-v2"
    },
    "OpenAI": {
        "api_url": "https://api.openai.com/v1",
        "model": "gpt-5.4-mini"
    },
    "阿里通义千问": {
        "api_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "model": "qwen-coder-turbo"
    },
    "字节跳动豆包": {
        "api_url": "https://ark.cn-beijing.volces.com/api/v3",
        "model": "doubao-seed-code-32k"
    },
    "百度文心一言": {
        "api_url": "https://qianfan.baidubce.com/v2",
        "model": "ernie-6.0-speed"
    },
    "硅基流动": {
        "api_url": "https://api.siliconflow.cn/v1",
        "model": "Qwen/Qwen2.5-7B-Instruct"
    },
    "自定义": {
        "api_url": "",
        "model": ""
    }
}

def compatibility_api_url(base_url):
    url = base_url.rstrip("/")
    if "generativelanguage" in url and "openai/chat/completions" not in url:
        url = url + "/openai/chat/completions"
    return url


def load_config():
    if not os.path.exists(CONFIG_FILE):
        save_config(dict(DEFAULT_CONFIG))
        return dict(DEFAULT_CONFIG)
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        cfg = json.load(f)
    if "model" not in cfg:
        cfg["model"] = DEFAULT_CONFIG["model"]
    return cfg


def save_config(config):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)


def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []


def save_history(messages):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)


def clear_history():
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)


def build_messages(user_message, context=None, system_override=None):
    config = load_config()

    if system_override:
        system = system_override
    else:
        system = config.get("system_prompt", DEFAULT_CONFIG["system_prompt"])
        if context:
            system += f"\n\n当前学习上下文：\n{context}"

    messages = [{"role": "system", "content": system}]

    history = load_history()
    for h in history[-6:]:
        messages.append(h)

    messages.append({"role": "user", "content": user_message})
    return messages


def _save_conversation(user_msg, reply):
    history = load_history()
    history.append({"role": "user", "content": user_msg})
    history.append({"role": "assistant", "content": reply})
    save_history(history[-20:])


def ask_ai(user_message, context=None, callback=None, max_tokens=None, temperature=None, system_override=None):
    config = load_config()
    api_key = config.get("api_key", "")
    if not api_key:
        return False, "请先在 AI 设置中配置 API 密钥"

    if not ensure_openai():
        return False, "缺少 openai 库，自动安装失败。请手动运行: pip install openai"

    base_url = compatibility_api_url(config.get("api_url", DEFAULT_CONFIG["api_url"]))
    model = config.get("model", DEFAULT_CONFIG["model"])
    messages = build_messages(user_message, context, system_override=system_override)

    try:
        from openai import OpenAI

        client = OpenAI(api_key=api_key, base_url=base_url)

        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature if temperature is not None else config.get("temperature", 0.7),
            max_tokens=max_tokens if max_tokens is not None else config.get("max_tokens", 2048),
            stream=False
        )

        reply = response.choices[0].message.content
        _save_conversation(user_message, reply)

        if callback:
            callback(reply)
        return True, reply

    except Exception as e:
        err_str = str(e)
        if "401" in err_str or "Unauthorized" in err_str or "认证" in err_str:
            return False, "API Key 错误或未授权，请检查 AI 设置中的密钥"
        if "402" in err_str or "Insufficient Balance" in err_str:
            return False, "账号余额不足，请充值"
        if "429" in err_str or "Rate limit" in err_str:
            return False, "请求频率过高，请稍后重试"
        if "500" in err_str:
            return False, "服务器内部错误，请稍后重试"
        if "503" in err_str:
            return False, "服务器繁忙，请稍后重试"
        if "Connection" in err_str or "timeout" in err_str.lower():
            return False, f"网络连接失败: {e}"
        return False, f"请求失败: {e}"


def ask_ai_stream(user_message, context=None, on_token=None, on_done=None, on_error=None):
    thread = threading.Thread(
        target=_stream_worker,
        args=(user_message, context, on_token, on_done, on_error),
        daemon=True
    )
    thread.start()
    return thread


def _stream_worker(user_message, context, on_token, on_done, on_error):
    config = load_config()
    api_key = config.get("api_key", "")
    if not api_key:
        if on_error:
            on_error("请先在 AI 设置中配置 API 密钥")
        return

    if not ensure_openai():
        if on_error:
            on_error("缺少 openai 库，自动安装失败。请手动运行: pip install openai")
        return

    base_url = compatibility_api_url(config.get("api_url", DEFAULT_CONFIG["api_url"]))
    model = config.get("model", DEFAULT_CONFIG["model"])
    messages = build_messages(user_message, context)

    try:
        from openai import OpenAI

        client = OpenAI(api_key=api_key, base_url=base_url)

        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=config.get("temperature", 0.7),
            max_tokens=config.get("max_tokens", 2048),
            stream=True
        )

        full_reply = ""
        for chunk in response:
            if chunk.choices and len(chunk.choices) > 0:
                delta = chunk.choices[0].delta
                if delta and delta.content:
                    content = delta.content
                    full_reply += content
                    if on_token:
                        on_token(content)

        if full_reply:
            _save_conversation(user_message, full_reply)
            if on_done:
                on_done(full_reply)
        else:
            if on_error:
                on_error("AI 返回了空内容，请检查模型名称是否正确")

    except Exception as e:
        err_str = str(e)
        if "401" in err_str:
            if on_error:
                on_error("API Key 错误或未授权，请检查 AI 设置中的密钥")
        elif "402" in err_str:
            if on_error:
                on_error("账号余额不足，请充值")
        elif "429" in err_str:
            if on_error:
                on_error("请求频率过高，请稍后重试")
        else:
            if on_error:
                on_error(f"请求失败: {e}")


def generate_tutor_prompt(lesson_name, step_concept, exercise_desc, user_code, result_info):
    prompt = f"【当前课程】{lesson_name}\n"
    prompt += f"【知识点】{step_concept}\n"
    if exercise_desc:
        prompt += f"【练习题】{exercise_desc}\n"
    if user_code:
        prompt += f"【学生代码】\n```\n{user_code}\n```\n"
    if result_info:
        prompt += f"【检查结果】{result_info}\n"
    prompt += "\n请根据以上信息，给出针对性的学习建议。如果代码有误请给提示让学生自己发现，不要直接给正确答案。"
    return prompt
