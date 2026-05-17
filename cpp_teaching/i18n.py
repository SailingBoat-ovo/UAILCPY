import json
import os

LANG_FILE = os.path.join(os.path.dirname(__file__), "lang_pref.json")

LANGUAGES = ["中文", "English"]

_STRINGS = {
    # ---- Window titles ----
    "main_title": {"中文": "AI C++/Python 学习工具", "English": "AI C++/Python Learning Tool"},
    "chat_title": {"中文": "AI交流", "English": "AI Chat"},
    "plan_title": {"中文": "AI规划课程", "English": "AI Course Plan"},
    "welcome_title": {"中文": "\U0001F389 \u6b22\u8fce", "English": "\U0001F389 Welcome"},
    "intro_title": {"中文": "\u5173\u4e8e\u672c\u7a0b\u5e8f", "English": "About This Program"},
    "calendar_title": {"中文": "\U0001F4C5 \u5b66\u4e60\u65e5\u5fd7", "English": "\U0001F4C5 Study Calendar"},
    "settings_title": {"中文": "AI \u6559\u5b66\u8bbe\u7f6e", "English": "AI Settings"},

    # ---- Top bar ----
    "lang_label": {"中文": "\u8bed\u8a00\uff1a", "English": "Language:"},
    "c_plus_plus": {"中文": "C++", "English": "C++"},
    "python": {"中文": "Python", "English": "Python"},
    "ai_settings": {"中文": "\u2699 AI\u8bbe\u7f6e", "English": "\u2699 AI Setup"},
    "ask_ai": {"中文": "\U0001F916 \u95eeAI\u8001\u5e08", "English": "\U0001F916 Ask AI"},
    "ai_plan": {"中文": "\U0001F9D0 AI\u89c4\u5212", "English": "\U0001F9D0 AI Plan"},
    "calendar_btn": {"中文": "\U0001F4C5 \u65e5\u5fd7", "English": "\U0001F4C5 Log"},
    "progress_fmt": {"中文": "\u8fdb\u5ea6\uff1a{}/{}\uff08{:.0f}%\uff09", "English": "Progress: {}/{} ({:.0f}%)"},

    # ---- Course tree ----
    "course_catalog": {"中文": "\U0001F4D6 \u8bfe\u7a0b\u76ee\u5f55", "English": "\U0001F4D6 Course Catalog"},
    "lesson_fmt": {"中文": "\u7b2c{}\u8bfe: {}", "English": "Lesson {}: {}"},
    "step_fmt": {"中文": "\u6b65\u9aa4 {}/{}", "English": "Step {}/{}"},

    # ---- Content area labels ----
    "example_code": {"中文": "\U0001F4BB \u793a\u4f8b\u4ee3\u7801", "English": "\U0001F4BB Example Code"},
    "exercise": {"中文": "\U0001F4DD \u7ec3\u4e60\u9898", "English": "\U0001F4DD Exercise"},
    "sample": {"中文": "\U0001F4C4 \u6837\u4f8b", "English": "\U0001F4C4 Sample"},
    "input_label": {"中文": "\U0001F4E5 \u8f93\u5165:", "English": "\U0001F4E5 Input:"},
    "expected_output": {"中文": "\U0001F4E4 \u671f\u671b\u8f93\u51fa:", "English": "\U0001F4E4 Expected Output:"},
    "your_code": {"中文": "\u270D\uFE0F \u4f60\u7684\u4ee3\u7801", "English": "\u270D\uFE0F Your Code"},
    "cpp_output": {"中文": "\U0001F4C4 C++ \u8f93\u51fa\u7c98\u8d34\u533a", "English": "\U0001F4C4 C++ Output Paste"},
    "cpp_output_tip": {"中文": "\u7528\u4f60\u7684\u7f16\u8bd1\u5668\u8fd0\u884c\u540e\u7c98\u8d34\u7ed3\u679c\u5230\u8fd9\u91cc", "English": "Compile & run with your compiler, then paste result here"},
    "check_result": {"中文": "\U0001F4AC \u68c0\u67e5\u7ed3\u679c", "English": "\U0001F4AC Check Result"},
    "no_sample_input": {"中文": "\uff08\u65e0\uff09", "English": "(none)"},

    # ---- Action buttons ----
    "prev_step": {"中文": "\u25c0 \u4e0a\u4e00\u6b65", "English": "\u25c0 Previous"},
    "run_check": {"中文": "\u25b6 \u8fd0\u884c\u68c0\u67e5", "English": "\u25b6 Run Check"},
    "show_answer": {"中文": "\u770b\u7b54\u6848", "English": "Answer"},
    "ai_help": {"中文": "\U0001F916 AI\u5e2e\u6211", "English": "\U0001F916 AI Help"},
    "skip": {"中文": "\u2935 \u8df3\u8fc7", "English": "\u2935 Skip"},
    "next_step": {"中文": "\u4e0b\u4e00\u6b65 \u25b6", "English": "Next \u25b6"},
    "reset_step": {"中文": "\u21bb \u91cd\u7f6e\u6b64\u8282", "English": "\u21bb Reset"},
    "step_fmt_full": {"中文": "\u7b2c{}\u8bfe: {}  |  \u6b65\u9aa4 {}/{}", "English": "Lesson {}: {}  |  Step {}/{}"},

    # ---- Language notes ----
    "lang_note_py": {"中文": "\u2139 Python\u5185\u7f6e\u6267\u884c\uff0c\u76f4\u63a5\u5199\u4ee3\u7801\u70b9\u8fd0\u884c\u68c0\u67e5\u5373\u53ef", "English": "\u2139 Python runs inline, just write code & check"},
    "lang_note_cpp": {"中文": "\u2139 \u7528\u4f60\u7684\u7f16\u8bd1\u5668\u7f16\u8bd1\u8fd0\u884c\u540e\uff0c\u5c06\u7ed3\u679c\u7c98\u8d34\u5230\u4e0b\u65b9\u518d\u70b9\u68c0\u67e5", "English": "\u2139 Compile with your compiler, paste output below & check"},
    "no_example": {"中文": "# \u65e0\u793a\u4f8b", "English": "# No example"},
    "write_hint_py": {"中文": "# \u8bf7\u5728\u6b64\u7f16\u5199\u4ee3\u7801\n", "English": "# Write your code here\n"},

    # ---- Check messages ----
    "check_no_code": {"中文": "\u8bf7\u5148\u7f16\u5199\u4ee3\u7801\uff01", "English": "Please write code first!"},
    "check_paste_cpp": {"中文": "\u8bf7\u5148\u7f16\u8bd1\u8fd0\u884cC++\uff0c\u5c06\u7ed3\u679c\u7c98\u8d34\u5230\u4e0b\u65b9", "English": "Compile & run C++ first, then paste result below"},
    "check_correct": {"中文": "\u2705 \u6b63\u786e\uff01\u7ee7\u7eed\u52a0\u6cb9\uff01", "English": "\u2705 Correct! Keep going!"},
    "check_wrong": {"中文": "\u274c \u8f93\u51fa\u4e0d\u5339\u914d\uff0c\u518d\u8bd5\u8bd5", "English": "\u274c Output mismatch, try again"},
    "show_answer_ok": {"中文": "\u5df2\u663e\u793a\u53c2\u8003\u7b54\u6848\uff0c\u53ef\u4ee5\u7ee7\u7eed\u4e0b\u4e00\u6b65", "English": "Reference answer shown, you can continue"},
    "answer_ref_cpp": {"中文": "// \u53c2\u8003\uff1a\u8f93\u51fa\u671f\u671b\u5185\u5bb9\n// {}", "English": "// Reference: expected output\n// {}"},

    # ---- Congratulations ----
    "congrats_title": {"中文": "\u606d\u559c\uff01", "English": "Congratulations!"},
    "congrats_msg": {"中文": "\u7b2c{}\u8bfe\u300c{}\u300d\u5b66\u4e60\u5b8c\u6210\uff01\n\u5f53\u524d\u8fdb\u5ea6\uff1a{}/{}", "English": "Lesson {} \u300c{}\u300d completed!\nCurrent progress: {}/{}"},
    "next_lesson_title": {"中文": "\u4e0b\u4e00\u8bfe", "English": "Next Lesson"},
    "next_lesson_ask": {"中文": "\u8fdb\u5165\u4e0b\u4e00\u8bfe\uff1a\u300c{}\u300d\uff1f", "English": "Go to next lesson: \u300c{}\u300d?"},

    # ---- Plan dialog ----
    "plan_title_label": {"中文": "\U0001F9D0 AI \u5c06\u4e3a\u4f60\u81ea\u4e3b\u89c4\u5212\u5b66\u4e60\u8bfe\u7a0b", "English": "\U0001F9D0 AI will plan your study course"},
    "plan_desc": {"中文": "\u8bf4\u660e\u4f60\u60f3\u5b66\u4e60\u7684\u5185\u5bb9\uff0cAI \u4f1a\u81ea\u52a8\u751f\u6210\u5b8c\u6574\u7684\u8bfe\u7a0b\u4f53\u7cfb\u5e76\u5c55\u793a\u5728\u76ee\u5f55\u4e2d\u3002", "English": "Describe what you want to learn, AI will generate a complete course structure."},
    "plan_example": {"中文": "\u4f8b\u5982\uff1a\u201c\u6211\u60f3\u4ece\u96f6\u5b66 C++\uff0c\u91cd\u70b9\u662f\u6307\u9488\u548c\u9762\u5411\u5bf9\u8c61\u201d", "English": "e.g.: \u201cLearn C++ from scratch, focus on pointers and OOP\u201d"},
    "plan_input_label": {"中文": "\u8bf7\u8f93\u5165\u4f60\u7684\u5b66\u4e60\u9700\u6c42", "English": "Enter your learning needs"},
    "plan_placeholder": {"中文": "\u6211\u60f3\u5b66 ", "English": "I want to learn "},
    "plan_thinking": {"中文": "\U0001F9D0 AI \u6b63\u5728\u601d\u8003\u5e76\u89c4\u5212\u8bfe\u7a0b...", "English": "\U0001F9D0 AI is thinking and planning..."},
    "plan_start": {"中文": "\U0001F9D0 \u5f00\u59cb\u89c4\u5212", "English": "\U0001F9D0 Start Planning"},
    "plan_cancel": {"中文": "\u53d6\u6d88", "English": "Cancel"},
    "plan_success": {"中文": "\u2705 \u6210\u529f\u751f\u6210 {} \u8282\u8bfe\uff01\u5df2\u6dfb\u52a0\u5230\u76ee\u5f55\u6811", "English": "\u2705 Generated {} lessons! Added to course tree"},
    "plan_need_key": {"中文": "\u8bf7\u5148\u70b9\u51fb\u201c\u2699 AI\u8bbe\u7f6e\u201d\u914d\u7f6eAPI\u5bc6\u94a5\uff01", "English": "Please configure API key in \u2699 AI Settings first!"},
    "plan_no_json": {"中文": "\u672a\u627e\u5230 JSON \u6570\u7ec4", "English": "No JSON array found"},
    "plan_parse_error": {"中文": "\u89e3\u6790\u5931\u8d25", "English": "Parse failed"},
    "plan_not_array": {"中文": "\u8fd4\u56de\u683c\u5f0f\u4e0d\u662f\u6570\u7ec4", "English": "Response is not an array"},
    "plan_too_few": {"中文": "\u8bfe\u7a0b\u6570\u91cf\u4e0d\u8db3\uff0c\u8bf7\u8f93\u5165\u66f4\u5177\u4f53\u7684\u5b66\u4e60\u9700\u6c42", "English": "Not enough lessons, please be more specific"},
    "plan_short": {"中文": "\u8bf7\u8f93\u5165\u66f4\u5177\u4f53\u7684\u5b66\u4e60\u9700\u6c42", "English": "Please enter a more specific request"},

    # ---- AI Settings ----
    "select_provider": {"中文": "\u9009\u62e9\u670d\u52a1\u5546\uff1a", "English": "Provider:"},
    "api_url": {"中文": "API \u5730\u5740\uff1a", "English": "API URL:"},
    "api_key_label": {"中文": "API Key\uff1a", "English": "API Key:"},
    "model_name": {"中文": "\u6a21\u578b\u540d\u79f0\uff1a", "English": "Model:"},
    "temperature": {"中文": "\u6e29\u5ea6 (0-2)\uff1a", "English": "Temperature (0-2):"},
    "ai_settings_tab_basic": {"中文": "\u57fa\u672c\u8bbe\u7f6e", "English": "Basic Settings"},
    "ai_settings_tab_prompt": {"中文": "\u6559\u5b66\u63d0\u793a\u8bcd", "English": "System Prompt"},
    "custom_prompt": {"中文": "\u81ea\u5b9a\u4e49AI\u6559\u5e08\u89d2\u8272\u63d0\u793a\u8bcd\uff1a\n\uff08\u53ef\u4ee5\u8bbe\u7f6eAI\u7684\u6559\u5b66\u98ce\u683c\u3001\u8bed\u8a00\u7b49\uff09", "English": "Custom AI teacher prompt:\n(Set AI teaching style, language, etc.)"},
    "save": {"中文": "\u4fdd\u5b58\u8bbe\u7f6e", "English": "Save Settings"},
    "test_connection": {"中文": "\u6d4b\u8bd5\u8fde\u63a5", "English": "Test Connection"},
    "save_success": {"中文": "AI\u8bbe\u7f6e\u5df2\u4fdd\u5b58\uff01", "English": "AI Settings saved!"},

    # ---- AI Chat ----
    "send": {"中文": "\u53d1\u9001", "English": "Send"},
    "clear_chat": {"中文": "\u6e05\u7a7a\u5bf9\u8bdd", "English": "Clear Chat"},
    "chat_placeholder": {"中文": "\u8f93\u5165\u4f60\u7684\u7f16\u7a0b\u95ee\u9898...", "English": "Ask a programming question..."},
    "chat_ai_busy": {"中文": "\u6b63\u5728\u8bf7\u6559AI\u8001\u5e08...", "English": "Asking AI teacher..."},
    "chat_ctx_lang": {"中文": "\u8bed\u8a00", "English": "Lang"},
    "chat_ctx_course": {"中文": "\u8bfe\u7a0b", "English": "Course"},
    "chat_ctx_step": {"中文": "\u6b65\u9aa4", "English": "Step"},

    # ---- Welcome ----
    "welcome_title_line1": {"中文": "\U0001F393 \u6b22\u8fce\u4f7f\u7528\u4eba\u5de5\u667a\u80fd", "English": "\U0001F393 Welcome to AI-Powered"},
    "welcome_title_line2": {"中文": "C++ / Python \u5b66\u4e60\u7a0b\u5e8f", "English": "C++ / Python Learning Program"},
    "welcome_dev_by": {"中文": "\U0001F92B \u672c\u7a0b\u5e8f\u7531\u4eba\u7c7b\u548c AI \u5171\u540c\u7814\u53d1", "English": "\U0001F92B Developed by Humans and AI"},
    "welcome_open_source": {"中文": "\U0001F4E6 \u672c\u7a0b\u5e8f\u5b8c\u5168\u5f00\u6e90\uff01", "English": "\U0001F4E6 Fully Open Source!"},
    "welcome_start": {"中文": "\U0001F680 \u5f00\u59cb\u5b66\u4e60", "English": "\U0001F680 Start Learning"},

    # ---- Intro / About ----
    "intro_architecture": {"中文": "\U0001F4BB \u6280\u672f\u67b6\u6784\u4e0e\u4ecb\u7ecd", "English": "\U0001F4BB Architecture & Introduction"},
    "intro_section_langs": {"中文": "\U0001F4D6 \u652f\u6301\u7684\u7f16\u7a0b\u8bed\u8a00", "English": "\U0001F4D6 Supported Languages"},
    "intro_section_learning": {"中文": "\U0001F578 \u5b66\u4e60\u539f\u7406\u4e0e\u6a21\u5f0f", "English": "\U0001F578 Learning Model"},
    "intro_section_ai": {"中文": "\U0001F9E0 AI \u667a\u80fd\u529f\u80fd", "English": "\U0001F9E0 AI Features"},
    "intro_section_goals": {"中文": "\U0001F4CA \u8bfe\u7a0b\u4f53\u7cfb\u4e0e\u76ee\u6807", "English": "\U0001F4CA Course System"},
    "intro_python": {"中文": "Python 3.x", "English": "Python 3.x"},
    "intro_python_desc": {"中文": "\u5185\u7f6e Python \u6267\u884c\u5668\uff0c\u53ef\u4ee5\u76f4\u63a5\u5728\u7a0b\u5e8f\u5185\u7f16\u5199\u3001\u8fd0\u884c\u548c\u68c0\u6d4b\u4ee3\u7801\u3002\u4ece\u57fa\u7840\u8bed\u6cd5\u5230\u9ad8\u7ea7\u7279\u6027\uff08\u51fd\u6570\u5f0f\u7f16\u7a0b\u3001\u88c5\u9970\u5668\u3001\u534f\u7a0b\u3001\u6790\u53e0\u5f0f\u7b49\uff09\u5168\u8986\u76d6\u3002", "English": "Built-in Python executor for writing, running & testing code inline. From basic syntax to advanced features (functional programming, decorators, coroutines, comprehensions, etc)."},
    "intro_cpp": {"中文": "C++ 17", "English": "C++ 17"},
    "intro_cpp_desc": {"中文": "\u5916\u90e8\u7f16\u8bd1\u5668\u652f\u6301\uff08GCC/MSVC/Clang\uff09\u3002\u63d0\u4f9b\u4ece C \u8bed\u8a00\u57fa\u7840\u3001\u6307\u9488\u3001\u5bb9\u5668\u3001\u9762\u5411\u5bf9\u8c61\u3001\u6a21\u677f\u3001STL \u5230 C++17 \u73b0\u4ee3\u7279\u6027\u7684\u5b8c\u6574\u8bfe\u7a0b\u3002", "English": "External compiler support (GCC/MSVC/Clang). Complete curriculum from C basics, pointers, containers, OOP, templates, STL to C++17 modern features."},
    "intro_guided": {"中文": "\u5206\u6b65\u5f15\u5bfc\u5f0f\u5b66\u4e60", "English": "Step-by-Step Learning"},
    "intro_guided_desc": {"中文": "\u6bcf\u8282\u8bfe\u6309\u7167\u300c\u6982\u5ff5\u8bb2\u89e3 \u2192 \u793a\u4f8b\u4ee3\u7801 \u2192 \u5b9e\u6218\u7ec3\u4e60\u300d\u7684\u7ed3\u6784\u7ec4\u7ec7\uff0c\u4ece\u5bb9\u5230\u96be\u5faa\u5e8f\u6e10\u8fdb\u3002\u652f\u6301\u4e0a\u4e00\u6b65\u3001\u4e0b\u4e00\u6b65\u3001\u8df3\u8fc7\u529f\u80fd\uff0c\u53ef\u4ee5\u5728\u8bfe\u7a0b\u5185\u4e1d\u6ed1\u5207\u6362\u3002", "English": "Each lesson follows Concept \u2192 Example Code \u2192 Practice Exercise. Supports prev/next/skip for smooth navigation within courses."},
    "intro_progress": {"中文": "\u5b66\u4e60\u8fdb\u5ea6\u4fdd\u5b58", "English": "Progress Persistence"},
    "intro_progress_desc": {"中文": "\u6240\u6709\u5b66\u4e60\u8fdb\u5ea6\u81ea\u52a8\u4fdd\u5b58\u5728\u672c\u5730\uff0c\u5173\u95ed\u7a0b\u5e8f\u540e\u4e0b\u6b21\u6253\u5f00\u81ea\u52a8\u6062\u590d\u5230\u4e0a\u6b21\u7684\u4f4d\u7f6e\u3002\u4e0d\u9700\u8981\u767b\u5f55\u548c\u7f51\u7edc\u8fde\u63a5\u3002", "English": "All progress saved locally. Auto-restores to your last position when reopening. No login or internet required."},
    "intro_check": {"中文": "\u4ee3\u7801\u8fd0\u884c\u4e0e\u68c0\u67e5", "English": "Code Execution & Checking"},
    "intro_check_desc": {"中文": "Python \u4ee3\u7801\u53ef\u4ee5\u76f4\u63a5\u5728\u7a0b\u5e8f\u5185\u8fd0\u884c\u5e76\u67e5\u770b\u8f93\u51fa\u3002C++ \u4ee3\u7801\u5728\u5916\u90e8\u7f16\u8bd1\u540e\u5c06\u8f93\u51fa\u7c98\u8d34\u56de\u6765\u8fdb\u884c\u68c0\u67e5\u3002\u652f\u6301\u81ea\u5b9a\u4e49\u8f93\u5165\u548c\u671f\u671b\u8f93\u51fa\u5bf9\u6bd4\u3002", "English": "Python runs inline with output shown directly. C++ compiled externally, paste results back for checking. Supports custom input and expected output comparison."},
    "intro_ai_tutor": {"中文": "AI \u667a\u80fd\u5bfc\u5e08", "English": "AI Tutor"},
    "intro_ai_tutor_desc": {"中文": "\u63a5\u5165\u591a\u79cd AI API\uff08\u5982 DeepSeek\u3001\u901a\u4e49\u5343\u95ee\u3001\u767e\u5ea6\u6587\u5fc3\u3001OpenAI \u7b49\uff09\uff0c\u5373\u65f6\u56de\u7b54\u7f16\u7a0b\u95ee\u9898\u3002\u53ef\u4ee5\u67e5\u770b\u5f53\u524d\u5b66\u4e60\u4e0a\u4e0b\u6587\uff0cAI \u4f1a\u6839\u636e\u4f60\u6b63\u5728\u5b66\u7684\u8bfe\u7a0b\u548c\u4ee3\u7801\u8fdb\u884c\u9488\u5bf9\u6027\u8f85\u5bfc\u3002", "English": "Connects to multiple AI APIs (DeepSeek, Qwen, Baidu, OpenAI, etc). Provides context-aware tutoring based on your current lesson and code."},
    "intro_ai_plan": {"中文": "AI \u81ea\u4e3b\u89c4\u5212\u8bfe\u7a0b", "English": "AI Course Planning"},
    "intro_ai_plan_desc": {"中文": "\u8f93\u5165\u4f60\u60f3\u5b66\u4e60\u7684\u5185\u5bb9\uff0cAI \u4f1a\u81ea\u52a8\u751f\u6210\u5b8c\u6574\u7684\u8bfe\u7a0b\u4f53\u7cfb\uff0c\u5305\u62ec\u6bcf\u8282\u8bfe\u7684\u6982\u5ff5\u3001\u793a\u4f8b\u4ee3\u7801\u548c\u7ec3\u4e60\u9898\u3002\u53ef\u4ee5\u81ea\u7531\u81ea\u5728\u5730\u6269\u5c55\u5b66\u4e60\u8fb9\u754c\u3002", "English": "Describe what you want to learn, AI generates a complete course with concepts, examples and exercises for each lesson."},
    "intro_ai_debug": {"中文": "\u4ee3\u7801\u8bc4\u5ba1\u4e0e\u8c03\u8bd5", "English": "Code Review & Debugging"},
    "intro_ai_debug_desc": {"中文": "AI \u53ef\u4ee5\u68c0\u67e5\u4f60\u7684\u4ee3\u7801\u9519\u8bef\uff0c\u7ed9\u51fa\u4fee\u6539\u5efa\u8bae\uff0c\u5e76\u89e3\u91ca\u4e3a\u4ec0\u4e48\u51fa\u9519\u3002\u5e2e\u52a9\u4f60\u7406\u89e3\u9519\u8bef\u7684\u6839\u672c\u539f\u56e0\uff0c\u800c\u4e0d\u662f\u7b80\u5355\u5730\u7ed9\u51fa\u7b54\u6848\u3002", "English": "AI checks your code, suggests fixes, and explains why it's wrong. Helps you understand the root cause rather than just giving answers."},
    "intro_zero": {"中文": "\u4ece\u96f6\u5230\u7cbe\u901a", "English": "Zero to Pro"},
    "intro_zero_desc": {"中文": "\u5185\u7f6e\u8bfe\u7a0b\u8986\u76d6\u4ece\u6700\u57fa\u7840\u7684\u8bed\u6cd5\u3001\u6570\u636e\u7c7b\u578b\uff0c\u5230\u9ad8\u7ea7\u7684\u7b97\u6cd5\u3001\u6570\u636e\u7ed3\u6784\u3001\u9762\u5411\u5bf9\u8c61\u3001\u51fd\u6570\u5f0f\u7f16\u7a0b\u3001\u5e76\u53d1\u7f16\u7a0b\u7b49\u3002\u9002\u5408\u5b8c\u5168\u96f6\u57fa\u7840\u7684\u65b0\u624b\u3002", "English": "Built-in courses cover basics (syntax, data types) to advanced topics (algorithms, data structures, OOP, functional & concurrent programming)."},
    "intro_comp": {"中文": "\u7ade\u8d5b\u7ea7\u522b", "English": "Competition Level"},
    "intro_comp_desc": {"中文": "\u8bfe\u7a0b\u5185\u5bb9\u8986\u76d6\u7ecf\u5178\u7b97\u6cd5\u9898\u76ee\u3001LeetCode \u9898\u578b\u3001ACM \u7ade\u8d5b\u6280\u5de7\u3001\u590d\u6742\u5ea6\u5206\u6790\u7b49\uff0c\u53ef\u4ee5\u7528\u4e8e\u7b97\u6cd5\u7ade\u8d5b\u548c\u804c\u4e1a\u9762\u8bd5\u51c6\u5907\u3002", "English": "Covers classic algorithm problems, LeetCode patterns, ACM competition techniques, and complexity analysis for competitive programming and interviews."},
    "intro_oss": {"中文": "\u5b8c\u5168\u5f00\u6e90", "English": "Open Source"},
    "intro_oss_desc": {"中文": "\u672c\u7a0b\u5e8f\u4f7f\u7528 MIT \u534f\u8bae\u5f00\u6e90\uff0c\u6bcf\u4e00\u884c\u4ee3\u7801\u90fd\u53ef\u67e5\u770b\u3001\u4fee\u6539\u3001\u5206\u53d1\u3002\u6b22\u8fce\u4e3a\u9879\u76ee\u8d21\u732e\u4ee3\u7801\u6216\u63d0\u4ea4 issue\u3002", "English": "MIT licensed. Every line of code is viewable, modifiable, and distributable. Contributions and issues welcome."},

    "close": {"中文": "\u5173\u95ed", "English": "Close"},
    "start_using": {"中文": "\U0001F680 \u5f00\u59cb\u4f7f\u7528", "English": "\U0001F680 Get Started"},

    # ---- Calendar ----
    "calendar_weekdays": {"中文": ["\u4e00", "\u4e8c", "\u4e09", "\u56db", "\u4e94", "\u516d", "\u65e5"], "English": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]},
    "calendar_month_title": {"中文": "{} \u5e74 {} \u6708", "English": "{} / {}"},
    "calendar_stats_month": {"中文": "\U0001F4CA \u672c\u6708\u7edf\u8ba1", "English": "\U0001F4CA This Month"},
    "calendar_stats_all": {"中文": "\U0001F3C6 \u5168\u90e8\u7d2f\u8ba1", "English": "\U0001F3C6 All Time"},
    "calendar_stat_fmt": {"中文": "\u5b66\u4e60 {} \u5929  |  \u5b8c\u6210 {} \u8282\u8bfe  |  {} \u4e2a\u6b65\u9aa4  |  {} \u6b21\u4ee3\u7801\u68c0\u67e5", "English": "{} days  |  {} lessons  |  {} steps  |  {} checks"},
    "calendar_stat_all_fmt": {"中文": "\u5b66\u4e60 {} \u5929  |  {} \u8282\u8bfe  |  {} \u6b65\u9aa4", "English": "{} days  |  {} lessons  |  {} steps"},

    # ---- Test connection ----
    "test_prompt": {"中文": "\u4f60\u662f\u4e00\u4e2a\u6d4b\u8bd5\u52a9\u624b", "English": "You are a test assistant"},
    "test_msg": {"中文": "\u8bf4\u4e00\u53e5\u8bdd\u544a\u8bc9\u6211\u4f60\u5df2\u7ecf\u8fde\u63a5\u6210\u529f\u4e86\u3002", "English": "Say one sentence to confirm connection is successful."},
    "test_ok": {"中文": "\u8fde\u63a5\u6210\u529f\uff01", "English": "Connection successful!"},
    "test_fail": {"中文": "\u8fde\u63a5\u5931\u8d25", "English": "Connection failed"},
    "test_key_empty": {"中文": "API Key \u4e0d\u80fd\u4e3a\u7a7a\uff01", "English": "API Key cannot be empty!"},
    "enter_lesson": {"中文": "\u8bf7\u5148\u8fdb\u5165\u4e00\u8282\u8bfe\u7a0b", "English": "Please select a lesson first"},
    "install_error": {"中文": "openai \u5e93\u5b89\u88c5\u5931\u8d25\uff0c\u8bf7\u624b\u52a8\u8fd0\u884c: pip install openai", "English": "openai library installation failed, please run: pip install openai"},
}


def _(key, *args):
    lang = load_lang_pref()
    strings = _STRINGS.get(key)
    if strings is None:
        return key
    text = strings.get(lang, strings.get("中文", key))
    if args:
        return text.format(*args)
    return text


def _list(key):
    lang = load_lang_pref()
    strings = _STRINGS.get(key)
    if strings is None:
        return key
    return strings.get(lang, strings.get("中文", key))


def load_lang_pref():
    if not os.path.exists(LANG_FILE):
        return "中文"
    try:
        with open(LANG_FILE, "r", encoding="utf-8") as f:
            return json.load(f).get("lang", "中文")
    except:
        return "中文"


def save_lang_pref(lang):
    with open(LANG_FILE, "w", encoding="utf-8") as f:
        json.dump({"lang": lang}, f, ensure_ascii=False, indent=2)
