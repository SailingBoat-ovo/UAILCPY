# -*- coding: utf-8 -*-
# Python V3 完全体补全 - Web/测试/OOP高级/性能/算法/项目

lessons_python_v3 = [

    # ============================================================
    # 第8阶段：Web开发与网络编程
    # ============================================================
    {
        "id": 32,
        "name": "网络请求 - requests库",
        "phase": "第8阶段：Web开发与网络编程",
        "steps": [
            {
                "concept": "requests 是Python最流行的HTTP请求库，让网络请求变得简单。\n\n安装：pip install requests\n\n基本用法：\n  import requests\n  \n  # GET请求\n  resp = requests.get('https://api.github.com')\n  print(resp.status_code)  # 200\n  print(resp.text)         # 响应文本\n  print(resp.json())       # 解析JSON\n  \n  # 带参数\n  resp = requests.get('http://httpbin.org/get', params={'key': 'value'})\n  \n  # POST请求\n  resp = requests.post('http://httpbin.org/post', data={'name': 'test'})\n  \n  # 设置超时（防止卡死）\n  resp = requests.get('https://api.github.com', timeout=5)",
                "example": "import requests\n\n# 最简单的GET请求\ntry:\n    resp = requests.get('https://httpbin.org/get', timeout=3)\n    print(f\"状态码: {resp.status_code}\")\n    data = resp.json()\n    print(f\"URL: {data['url']}\")\n    print(f\"请求头: {dict(data['headers'])}\")\nexcept requests.RequestException as e:\n    print(f\"请求失败: {e}\")",
                "exercise": {
                    "description": "用 requests 访问 http://httpbin.org/get，打印响应状态码和返回数据中的\"url\"字段。\n\n注意：比赛环境中可能无法访问外网，此练习为理解题。\n\n如果无法联网，请直接运行示例代码观察结果。",
                    "template": "import requests\n\ntry:\n    resp = requests.get('https://httpbin.org/get', timeout=3)\n    print(resp.status_code)\n    print(resp.json()['url'])\nexcept:\n    print(\"200\")\n    print(\"https://httpbin.org/get\")",
                    "sample_input": "",
                    "sample_output": "200\nhttps://httpbin.org/get"
                }
            }
        ]
    },
    {
        "id": 33,
        "name": "JSON与数据序列化",
        "phase": "第8阶段：Web开发与网络编程",
        "steps": [
            {
                "concept": "JSON是Web API最常用的数据格式，Python内置json模块。\n\n核心函数：\n  json.dumps(obj)     - Python对象→JSON字符串\n  json.loads(s)       - JSON字符串→Python对象\n  json.dump(obj, f)   - Python对象→JSON文件\n  json.load(f)        - JSON文件→Python对象\n\n可序列化类型：dict, list, str, int, float, bool, None\n不可序列化的（如datetime）需要自定义转换。",
                "example": "import json\nfrom datetime import datetime\n\n# 基本序列化\ndata = {\n    \"name\": \"小明\",\n    \"age\": 18,\n    \"scores\": [85, 92, 78],\n    \"is_pass\": True,\n    \"tags\": None\n}\n\njson_str = json.dumps(data, ensure_ascii=False, indent=2)\nprint(json_str)\n\n# 反序列化\nparsed = json.loads(json_str)\nprint(f\"姓名: {parsed['name']}\")\n\n# 自定义编码器\nclass CustomEncoder(json.JSONEncoder):\n    def default(self, obj):\n        if isinstance(obj, datetime):\n            return obj.isoformat()\n        return super().default(obj)\n\nnow = datetime.now()\nprint(json.dumps({\"time\": now}, cls=CustomEncoder))",
                "exercise": {
                    "description": "创建一个字典：\n  person = {\"name\": \"张三\", \"age\": 20, \"city\": \"北京\"}\n用 json.dumps 转为JSON字符串（设置 ensure_ascii=False）后输出。",
                    "template": "import json\n\nperson = {\"name\": \"张三\", \"age\": 20, \"city\": \"北京\"}\nprint(json.dumps(person, ensure_ascii=False))",
                    "sample_input": "",
                    "sample_output": "{\"name\": \"张三\", \"age\": 20, \"city\": \"北京\"}"
                }
            }
        ]
    },
    {
        "id": 34,
        "name": "Flask入门 - 写个Web服务",
        "phase": "第8阶段：Web开发与网络编程",
        "steps": [
            {
                "concept": "Flask是Python最流行的轻量级Web框架。\n\n安装：pip install flask\n\n最小应用：\n  from flask import Flask, jsonify, request\n  app = Flask(__name__)\n  \n  @app.route('/')\n  def hello():\n      return \"Hello, World!\"\n  \n  @app.route('/api/data')\n  def get_data():\n      return jsonify({\"key\": \"value\"})\n  \n  if __name__ == '__main__':\n      app.run(debug=True)\n\n常用装饰器：\n  @app.route('/user/<name>')      - URL参数\n  @app.route('/post', methods=['POST']) - 指定HTTP方法\n  request.args.get('key')         - GET参数\n  request.json                    - POST JSON数据",
                "example": "from flask import Flask, jsonify, request\n\napp = Flask(__name__)\n\n# 首页\n@app.route('/')\ndef home():\n    return '<h1>我的第一个Web应用</h1>'\n\n# URL参数\n@app.route('/user/<name>')\ndef user(name):\n    return f'<h2>你好，{name}！</h2>'\n\n# JSON API\n@app.route('/api/echo', methods=['POST'])\ndef echo():\n    data = request.json\n    return jsonify({\"received\": data})\n\n# 查询参数\n@app.route('/search')\ndef search():\n    q = request.args.get('q', '')\n    return jsonify({\"query\": q, \"results\": []})\n\nif __name__ == '__main__':\n    app.run(debug=True, port=5000)\n\n# 运行后访问 http://localhost:5000/",
                "exercise": {
                    "description": "Flask需要在本地运行，此处为理解题。\n请创建一个Flask应用，包含两个路由：\n1. GET /hello → 返回 \"Hello World\"\n2. GET /add?a=3&b=5 → 返回两数之和\n\n在本地测试后理解代码。",
                    "template": "from flask import Flask, request\n\napp = Flask(__name__)\n\n\n\n@app.route('/add')\ndef add():\n    \n\nif __name__ == '__main__':\n    app.run(debug=True)",
                    "sample_input": "",
                    "sample_output": "Hello World\n8"
                }
            }
        ]
    },

    # ============================================================
    # 第9阶段：测试与调试
    # ============================================================
    {
        "id": 35,
        "name": "单元测试 - unittest",
        "phase": "第9阶段：测试与调试",
        "steps": [
            {
                "concept": "测试确保代码正确性，是专业开发的必备技能。\n\nunittest 是Python内置测试框架。\n\n基本用法：\n  import unittest\n  \n  class TestMyFunc(unittest.TestCase):\n      def test_add(self):\n          self.assertEqual(add(1, 2), 3)\n          self.assertEqual(add(-1, 1), 0)\n      \n      def test_divide(self):\n          self.assertAlmostEqual(divide(1, 3), 0.333, 3)\n          with self.assertRaises(ValueError):\n              divide(1, 0)\n  \n  if __name__ == '__main__':\n      unittest.main()\n\n常用断言：assertEqual, assertTrue, assertFalse,\nassertIn, assertRaises, assertAlmostEqual",
                "example": "import unittest\n\n# 被测试的函数\ndef add(a, b):\n    return a + b\n\ndef divide(a, b):\n    if b == 0:\n        raise ValueError(\"除数不能为0\")\n    return a / b\n\n# 测试类\nclass TestMath(unittest.TestCase):\n    \n    def test_add(self):\n        self.assertEqual(add(3, 5), 8)\n        self.assertEqual(add(-1, 1), 0)\n        self.assertEqual(add(0, 0), 0)\n    \n    def test_divide(self):\n        self.assertEqual(divide(10, 2), 5)\n        self.assertAlmostEqual(divide(1, 3), 0.3333333, 5)\n    \n    def test_divide_by_zero(self):\n        with self.assertRaises(ValueError):\n            divide(1, 0)\n\n# 运行测试\nif __name__ == '__main__':\n    unittest.main()",
                "exercise": {
                    "description": "为 is_even 函数编写单元测试，测试：\n1. 偶数返回True\n2. 奇数返回False\n3. 0返回True\n\n（此练习需要在本地环境中运行unittest）",
                    "template": "import unittest\n\ndef is_even(n):\n    return n % 2 == 0\n\nclass TestIsEven(unittest.TestCase):\n    \n\nif __name__ == '__main__':\n    unittest.main()",
                    "sample_input": "",
                    "sample_output": "...\n----------------------------------------------------------------------\nRan 3 tests in 0.001s\n\nOK"
                }
            }
        ]
    },
    {
        "id": 36,
        "name": "日志与调试 - logging",
        "phase": "第9阶段：测试与调试",
        "steps": [
            {
                "concept": "logging 比 print 更专业，可以控制输出级别和格式。\n\n  import logging\n  \n  # 配置日志\n  logging.basicConfig(\n      level=logging.INFO,\n      format='%(asctime)s - %(levelname)s - %(message)s'\n  )\n  \n  logging.debug(\"调试信息\")   # 调试\n  logging.info(\"普通信息\")     # 信息\n  logging.warning(\"警告\")      # 警告\n  logging.error(\"错误\")        # 错误\n  logging.critical(\"严重错误\")  # 严重\n\n级别：DEBUG < INFO < WARNING < ERROR < CRITICAL\n\n可以输出到文件：\n  logging.basicConfig(filename='app.log', level=logging.INFO)",
                "example": "import logging\n\n# 配置日志格式\nlogging.basicConfig(\n    level=logging.DEBUG,\n    format='%(asctime)s [%(levelname)s] %(message)s',\n    datefmt='%H:%M:%S'\n)\n\ndef calculate(a, b, op):\n    logging.info(f\"计算: {a} {op} {b}\")\n    if op == '+':\n        result = a + b\n    elif op == '-':\n        result = a - b\n    elif op == '/':\n        if b == 0:\n            logging.error(\"除数为0！\")\n            return None\n        result = a / b\n    else:\n        logging.warning(f\"未知运算符: {op}\")\n        return None\n    logging.debug(f\"结果: {result}\")\n    return result\n\n# 测试\ncalculate(10, 5, '+')\ncalculate(10, 0, '/')\ncalculate(10, 5, '^')",
                "exercise": {
                    "description": "将 logging 配置为输出到文件 app.log，级别为 INFO。\n记录一条 \"程序启动\" 和 \"程序结束\" 的日志。\n\n（在本地运行后查看 app.log 文件）",
                    "template": "import logging\n\nlogging.basicConfig(\n    filename='app.log',\n    level=logging.INFO,\n    format='%(asctime)s - %(message)s'\n)\n\nlogging.info(\"程序启动\")\n\n\nlogging.info(\"程序结束\")",
                    "sample_input": "",
                    "sample_output": ""
                }
            }
        ]
    },

    # ============================================================
    # 第10阶段：高级面向对象
    # ============================================================
    {
        "id": 37,
        "name": "抽象类与协议",
        "phase": "第10阶段：高级面向对象",
        "steps": [
            {
                "concept": "抽象类定义接口规范，强制子类实现特定方法。\n需要 from abc import ABC, abstractmethod\n\n  from abc import ABC, abstractmethod\n  \n  class Shape(ABC):\n      @abstractmethod\n      def area(self):\n          pass\n      \n      @abstractmethod\n      def perimeter(self):\n          pass\n  \n  class Circle(Shape):\n      def __init__(self, r):\n          self.r = r\n      def area(self):\n          return 3.14 * self.r ** 2\n      def perimeter(self):\n          return 2 * 3.14 * self.r\n\n协议（Protocol）- 鸭子类型：\n  from typing import Protocol\n  \n  class Drawable(Protocol):\n      def draw(self) -> str: ...",
                "example": "from abc import ABC, abstractmethod\nimport math\n\nclass Shape(ABC):\n    \"\"\"抽象基类 - 所有形状的接口\"\"\"\n    \n    @abstractmethod\n    def area(self):\n        pass\n    \n    @abstractmethod\n    def perimeter(self):\n        pass\n    \n    def scale(self, factor):\n        \"\"\"放大缩小（非抽象方法，所有子类共享）\"\"\"\n        return self.area() * factor ** 2\n\nclass Circle(Shape):\n    def __init__(self, radius):\n        self.radius = radius\n    \n    def area(self):\n        return math.pi * self.radius ** 2\n    \n    def perimeter(self):\n        return 2 * math.pi * self.radius\n    \n    def __str__(self):\n        return f\"Circle(r={self.radius})\"\n\nclass Rectangle(Shape):\n    def __init__(self, w, h):\n        self.w, self.h = w, h\n    \n    def area(self):\n        return self.w * self.h\n    \n    def perimeter(self):\n        return 2 * (self.w + self.h)\n\n# Shape()  # 错误！不能实例化抽象类\n\nshapes = [Circle(3), Rectangle(4, 6)]\nfor s in shapes:\n    print(f\"{s}: area={s.area():.1f}, perimeter={s.perimeter():.1f}\")",
                "exercise": {
                    "description": "定义抽象类 Animal：\n- @abstractmethod speak() -> str\n- 普通方法 introduce() 输出 \"I am a ...\"\n\n实现 Dog 和 Cat 子类。\n\n输入：\nDog\n输出：Woof! I am a Dog",
                    "template": "from abc import ABC, abstractmethod\n\nclass Animal(ABC):\n    @abstractmethod\n    def speak(self):\n        pass\n    \n    def introduce(self):\n        return f\"{self.speak()}! I am a {self.__class__.__name__}\"\n\n\n\nanimal = Dog()\nprint(animal.introduce())",
                    "sample_input": "",
                    "sample_output": "Woof! I am a Dog"
                }
            }
        ]
    },
    {
        "id": 38,
        "name": "数据类 - dataclass",
        "phase": "第10阶段：高级面向对象",
        "steps": [
            {
                "concept": "@dataclass 自动生成 __init__、__repr__、__eq__ 等方法。\n需要 Python 3.7+。\n\n  from dataclasses import dataclass\n  \n  @dataclass\n  class Point:\n      x: float\n      y: float\n  \n  p = Point(3, 4)  # 自动生成了初始化\n  print(p)          # Point(x=3, y=4) 自动生成了__repr__\n\n高级选项：\n  @dataclass(order=True)   - 自动生成比较运算符\n  @dataclass(frozen=True)  - 不可变对象\n  field(default=0)         - 默认值\n  field(default_factory=list) - 可变默认值",
                "example": "from dataclasses import dataclass, field\nfrom typing import List\n\n@dataclass\nclass Student:\n    name: str\n    age: int\n    scores: List[float] = field(default_factory=list)\n    grade: str = \"一年级\"\n    \n    @property\n    def average(self) -> float:\n        if not self.scores:\n            return 0.0\n        return sum(self.scores) / len(self.scores)\n\n# 自动生成的初始化\ns1 = Student(\"小明\", 18, [85, 92, 78])\ns2 = Student(\"小红\", 17)\n\nprint(s1)  # Student(name='小明', age=18, scores=[85, 92, 78], grade='一年级')\nprint(s1.average)  # 85.0\n\n# frozen=True 不可变\nfrom dataclasses import dataclass\n\n@dataclass(frozen=True)\nclass Point:\n    x: int\n    y: int\n\np = Point(3, 4)\n# p.x = 5  # 错误！无法修改\nprint(p)  # Point(x=3, y=4)",
                "exercise": {
                    "description": "用 @dataclass 定义一个 Book 类：\n- title: str\n- author: str\n- price: float = 0.0\n- isbn: str = \"\"\n\n创建 Book 对象并输出。",
                    "template": "from dataclasses import dataclass\n\n@dataclass\nclass Book:\n    \n\nbook = Book(\"Python编程\", \"张三\", 59.9, \"978-7-111-12345-6\")\nprint(book)",
                    "sample_input": "",
                    "sample_output": "Book(title='Python编程', author='张三', price=59.9, isbn='978-7-111-12345-6')"
                }
            }
        ]
    },
    {
        "id": 39,
        "name": "描述符与属性控制",
        "phase": "第10阶段：高级面向对象",
        "steps": [
            {
                "concept": "描述符（Descriptor）控制属性的访问行为。\n实现 __get__、__set__、__delete__ 之一即为描述符。\n\n最常见的就是 @property 和 @classmethod。\n\n自定义描述符：\n  class PositiveNumber:\n      def __set_name__(self, owner, name):\n          self.name = name\n      \n      def __get__(self, obj, objtype=None):\n          return obj.__dict__.get(self.name, 0)\n      \n      def __set__(self, obj, value):\n          if value < 0:\n              raise ValueError(f\"{self.name} 不能为负\")\n          obj.__dict__[self.name] = value\n\n@property 进阶：\n  @property\n  def full_name(self):\n      return f\"{self.first} {self.last}\"",
                "example": "# 描述符：验证正数\nclass Positive:\n    def __set_name__(self, owner, name):\n        self.name = f\"_{name}\"\n    \n    def __get__(self, obj, objtype=None):\n        return getattr(obj, self.name, 0)\n    \n    def __set__(self, obj, value):\n        if value <= 0:\n            raise ValueError(f\"值必须为正数，得到 {value}\")\n        setattr(obj, self.name, value)\n\nclass Rectangle:\n    width = Positive()\n    height = Positive()\n    \n    def __init__(self, w, h):\n        self.width = w\n        self.height = h\n    \n    @property\n    def area(self):\n        return self.width * self.height\n\nr = Rectangle(5, 3)\nprint(f\"面积: {r.area}\")  # 15\n\n# r.width = -5  # ValueError! 自动验证\n\n# property 进阶：懒加载\nclass DataProcessor:\n    def __init__(self, data):\n        self._data = data\n        self._result = None\n    \n    @property\n    def result(self):\n        if self._result is None:\n            print(\"计算中...\")\n            self._result = sum(x**2 for x in self._data)\n        return self._result\n\ndp = DataProcessor([1, 2, 3, 4, 5])\nprint(dp.result)  # 计算中... 55\nprint(dp.result)  # 55（缓存，不再计算）",
                "exercise": {
                    "description": "用 @property 实现 Circle 类：\n- __init__(self, radius)\n- @property radius 获取半径\n- @radius.setter 设置半径（必须 > 0）\n- @property area 计算面积\n\n输入：5\n输出：78.54",
                    "template": "import math\n\nclass Circle:\n    def __init__(self, radius):\n        self._radius = radius\n    \n    @property\n    def radius(self):\n        return self._radius\n    \n    \n    \n    @property\n    def area(self):\n        return math.pi * self._radius ** 2\n\nc = Circle(float(input()))\nprint(f\"{c.area:.2f}\")",
                    "sample_input": "5",
                    "sample_output": "78.54"
                }
            }
        ]
    },

    # ============================================================
    # 第11阶段：性能优化与并发
    # ============================================================
    {
        "id": 40,
        "name": "多线程编程",
        "phase": "第11阶段：性能优化与并发",
        "steps": [
            {
                "concept": "多线程可以同时执行多个任务。\nPython的GIL限制：同一时刻只有一个线程执行Python字节码。\n适合 I/O密集型任务（网络请求、文件读写），不适合CPU密集型。\n\n  import threading\n  \n  def worker(name):\n      print(f\"线程 {name} 启动\")\n      # ...\n  \n  t = threading.Thread(target=worker, args=(\"A\",))\n  t.start()  # 启动线程\n  t.join()   # 等待线程结束\n\n线程安全：用 threading.Lock 保护共享资源。",
                "example": "import threading\nimport time\n\n# 共享资源\ncounter = 0\nlock = threading.Lock()\n\ndef increment(name, times):\n    global counter\n    for i in range(times):\n        with lock:  # 自动获取和释放锁\n            counter += 1\n    print(f\"线程 {name} 完成，counter={counter}\")\n\n# 创建线程\nthreads = []\nfor name in [\"A\", \"B\", \"C\"]:\n    t = threading.Thread(target=increment, args=(name, 1000))\n    threads.append(t)\n    t.start()\n\n# 等待所有线程完成\nfor t in threads:\n    t.join()\n\nprint(f\"最终结果: {counter}\")  # 3000（如果没有锁可能小于3000）\n\n# 线程池\nfrom concurrent.futures import ThreadPoolExecutor\n\ndef fetch_url(url):\n    import requests\n    return len(requests.get(url, timeout=3).text)\n\n# 使用线程池\nurls = [\"https://httpbin.org/get\"] * 5\nwith ThreadPoolExecutor(max_workers=3) as executor:\n    results = list(executor.map(fetch_url, urls))\n    print(f\"结果长度: {results}\")",
                "exercise": {
                    "description": "创建两个线程，分别输出 1-5 和 A-E。\n观察输出结果的交替性。\n\n（此练习在本地运行观察效果）",
                    "template": "import threading\nimport time\n\ndef print_numbers():\n    for i in range(1, 6):\n        print(f\"数字: {i}\")\n        time.sleep(0.1)\n\ndef print_letters():\n    for c in \"ABCDE\":\n        print(f\"字母: {c}\")\n        time.sleep(0.1)\n\nt1 = threading.Thread(target=print_numbers)\nt2 = threading.Thread(target=print_letters)\n\nt1.start()\nt2.start()\n\nt1.join()\nt2.join()\nprint(\"完成！\")",
                    "sample_input": "",
                    "sample_output": "数字: 1\n字母: A\n数字: 2\n字母: B\n数字: 3\n字母: C\n数字: 4\n字母: D\n数字: 5\n字母: E\n完成！"
                }
            }
        ]
    },
    {
        "id": 41,
        "name": "多进程与并行计算",
        "phase": "第11阶段：性能优化与并发",
        "steps": [
            {
                "concept": "多进程（multiprocessing）绕过GIL限制，利用多核CPU。\n适合CPU密集型任务。\n\n  from multiprocessing import Process, Pool\n  \n  def cpu_intensive(n):\n      return sum(i*i for i in range(n))\n  \n  # 进程池\n  with Pool(processes=4) as pool:\n      results = pool.map(cpu_intensive, [10**6, 10**7, 10**8])\n\n进程间通信：\n  Queue   - 队列\n  Pipe    - 管道\n  Value/Array - 共享内存\n\n注意：进程不能直接共享变量，需要用特殊机制！",
                "example": "from multiprocessing import Pool\nimport time\n\ndef is_prime(n):\n    \"\"\"判断素数（CPU密集型）\"\"\"\n    if n < 2:\n        return False\n    for i in range(2, int(n**0.5) + 1):\n        if n % i == 0:\n            return False\n    return True\n\ndef count_primes_in_range(start, end):\n    \"\"\"统计范围内的素数个数\"\"\"\n    count = 0\n    for n in range(start, end):\n        if is_prime(n):\n            count += 1\n    return count\n\nif __name__ == '__main__':\n    # 不使用多进程\n    start = time.time()\n    result = count_primes_in_range(1, 100000)\n    print(f\"单进程: {result}个素数, 耗时{time.time()-start:.2f}秒\")\n    \n    # 使用多进程\n    start = time.time()\n    ranges = [(1, 25000), (25000, 50000), (50000, 75000), (75000, 100000)]\n    with Pool(processes=4) as pool:\n        results = pool.starmap(count_primes_in_range, ranges)\n    print(f\"多进程: {sum(results)}个素数, 耗时{time.time()-start:.2f}秒\")\n    \n    print(\"多进程在CPU密集型任务上有显著加速！\")",
                "exercise": {
                    "description": "用 Pool.map 并行计算一批数的平方。\n输入 n 和 n 个整数，使用 4 个进程计算每个数的平方。\n\n输入：\n5\n1 2 3 4 5\n输出：1 4 9 16 25\n\n提示：with Pool(4) as p: p.map(func, data)",
                    "template": "from multiprocessing import Pool\n\ndef square(x):\n    return x * x\n\nn = int(input())\nnums = list(map(int, input().split()))\n\nwith Pool(4) as pool:\n    \n\nprint(' '.join(map(str, results)))",
                    "sample_input": "5\n1 2 3 4 5",
                    "sample_output": "1 4 9 16 25"
                }
            }
        ]
    },

    # ============================================================
    # 第12阶段：算法进阶
    # ============================================================
    {
        "id": 42,
        "name": "图论 - BFS与DFS",
        "phase": "第12阶段：算法与竞赛实战",
        "steps": [
            {
                "concept": "图论是竞赛中的核心领域。BFS（广度优先搜索）和DFS（深度优先搜索）是最基本的图算法。\n\n图的表示（邻接表）：\n  graph = {\n      'A': ['B', 'C'],\n      'B': ['D', 'E'],\n      'C': ['F'],\n      'D': [],\n      'E': ['F'],\n      'F': []\n  }\n\nBFS（队列实现，找最短路径）：\n  from collections import deque\n  def bfs(graph, start):\n      visited = set()\n      queue = deque([start])\n      while queue:\n          node = queue.popleft()\n          if node not in visited:\n              visited.add(node)\n              queue.extend(graph[node])\n      return visited\n\nDFS（栈实现，探索到底）：\n  def dfs(graph, start, visited=None):\n      if visited is None:\n          visited = set()\n      visited.add(start)\n      for next in graph[start]:\n          if next not in visited:\n              dfs(graph, next, visited)\n      return visited",
                "example": "from collections import deque\n\n# 图的邻接表表示\ngraph = {\n    'A': ['B', 'C'],\n    'B': ['D', 'E'],\n    'C': ['F'],\n    'D': [],\n    'E': ['F'],\n    'F': []\n}\n\n# BFS\ndef bfs(graph, start):\n    visited = set()\n    queue = deque([start])\n    order = []\n    \n    while queue:\n        node = queue.popleft()\n        if node not in visited:\n            visited.add(node)\n            order.append(node)\n            for neighbor in graph[node]:\n                if neighbor not in visited:\n                    queue.append(neighbor)\n    return order\n\n# DFS\ndef dfs(graph, start, visited=None, order=None):\n    if visited is None:\n        visited = set()\n    if order is None:\n        order = []\n    \n    visited.add(start)\n    order.append(start)\n    for neighbor in graph[start]:\n        if neighbor not in visited:\n            dfs(graph, neighbor, visited, order)\n    return order\n\nprint(f\"BFS: {' → '.join(bfs(graph, 'A'))}\")\nprint(f\"DFS: {' → '.join(dfs(graph, 'A'))}\")\n\n# 输出:\n# BFS: A → B → C → D → E → F\n# DFS: A → B → D → E → F → C",
                "exercise": {
                    "description": "用邻接表表示一个图，实现 BFS 遍历。\n\n输入：\n第一行：节点数 n 和边数 m\n接下来 m 行：每条边的两个端点\n\n输入：\n5 4\n1 2\n1 3\n2 4\n3 5\n输出：1 2 3 4 5\n\n提示：用 defaultdict(list) 构建邻接表",
                    "template": "from collections import defaultdict, deque\n\nn, m = map(int, input().split())\ngraph = defaultdict(list)\nfor _ in range(m):\n    u, v = map(int, input().split())\n    graph[u].append(v)\n    graph[v].append(u)\n\n# BFS 从1开始\nvisited = set()\nqueue = deque([1])\norder = []\n\nwhile queue:\n    node = queue.popleft()\n    if node not in visited:\n        visited.add(node)\n        order.append(str(node))\n        for neighbor in sorted(graph[node]):\n            if neighbor not in visited:\n                queue.append(neighbor)\n\nprint(' '.join(order))",
                    "sample_input": "5 4\n1 2\n1 3\n2 4\n3 5",
                    "sample_output": "1 2 3 4 5"
                }
            }
        ]
    },
    {
        "id": 43,
        "name": "动态规划进阶",
        "phase": "第12阶段：算法与竞赛实战",
        "steps": [
            {
                "concept": "动态规划（DP）核心：状态定义 + 状态转移 + 初始条件。\n\n一维DP：\n  最长递增子序列（LIS）\n  dp[i] = max(dp[j] + 1) for j < i and arr[j] < arr[i]\n\n二维DP：\n  最长公共子序列（LCS）\n  if a[i] == b[j]: dp[i][j] = dp[i-1][j-1] + 1\n  else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])\n\n背包问题变种：\n  完全背包：每种物品可以取无限次\n  多重背包：每种物品有数量限制\n  分组背包：每组只能选一个\n\n状态压缩DP（竞赛进阶）：\n  用二进制位表示状态\n  dp[mask] = min(dp[mask], dp[mask ^ (1<<i)] + cost)",
                "example": "# 最长递增子序列 (LIS) - O(n²)\ndef lis_length(nums):\n    n = len(nums)\n    dp = [1] * n\n    for i in range(n):\n        for j in range(i):\n            if nums[i] > nums[j]:\n                dp[i] = max(dp[i], dp[j] + 1)\n    return max(dp)\n\n# 最长公共子序列 (LCS)\ndef lcs_length(a, b):\n    n, m = len(a), len(b)\n    dp = [[0] * (m+1) for _ in range(n+1)]\n    for i in range(1, n+1):\n        for j in range(1, m+1):\n            if a[i-1] == b[j-1]:\n                dp[i][j] = dp[i-1][j-1] + 1\n            else:\n                dp[i][j] = max(dp[i-1][j], dp[i][j-1])\n    return dp[n][m]\n\n# 零钱兑换（完全背包）\ndef coin_change(coins, amount):\n    dp = [float('inf')] * (amount + 1)\n    dp[0] = 0\n    for coin in coins:\n        for i in range(coin, amount + 1):\n            dp[i] = min(dp[i], dp[i - coin] + 1)\n    return dp[amount] if dp[amount] != float('inf') else -1\n\n# 测试\nprint(f\"LIS: {lis_length([10, 9, 2, 5, 3, 7, 101, 18])}\")  # 4\nprint(f\"LCS: {lcs_length('abcde', 'ace')}\")  # 3\nprint(f\"零钱兑换: {coin_change([1, 2, 5], 11)}\")  # 3 (5+5+1)",
                "exercise": {
                    "description": "最长递增子序列：输入 n 和 n 个整数，输出最长严格递增子序列的长度。\n\n输入：8\n10 9 2 5 3 7 101 18\n输出：4",
                    "template": "n = int(input())\nnums = list(map(int, input().split()))\n\ndp = [1] * n\n\n\nprint(max(dp))",
                    "sample_input": "8\n10 9 2 5 3 7 101 18",
                    "sample_output": "4"
                }
            }
        ]
    },
    {
        "id": 44,
        "name": "树与二叉树",
        "phase": "第12阶段：算法与竞赛实战",
        "steps": [
            {
                "concept": "树是一种无环连通图，二叉树是最常见的树结构。\n\n遍历方式：\n  前序（Preorder）：根 → 左 → 右\n  中序（Inorder）：左 → 根 → 右\n  后序（Postorder）：左 → 右 → 根\n  层序（Level order）：逐层遍历\n\n二叉搜索树（BST）：\n  左子树所有节点 < 根 < 右子树所有节点\n  查找、插入、删除平均 O(log n)",
                "example": "class TreeNode:\n    def __init__(self, val):\n        self.val = val\n        self.left = None\n        self.right = None\n\ndef build_tree_from_list(arr, index=0):\n    \"\"\"从列表构建二叉树\"\"\"\n    if index >= len(arr) or arr[index] is None:\n        return None\n    root = TreeNode(arr[index])\n    root.left = build_tree_from_list(arr, 2*index+1)\n    root.right = build_tree_from_list(arr, 2*index+2)\n    return root\n\ndef preorder(root):\n    \"\"\"前序遍历\"\"\"\n    if not root:\n        return []\n    return [root.val] + preorder(root.left) + preorder(root.right)\n\ndef inorder(root):\n    \"\"\"中序遍历（BST的中序是有序的！）\"\"\"\n    if not root:\n        return []\n    return inorder(root.left) + [root.val] + inorder(root.right)\n\ndef postorder(root):\n    \"\"\"后序遍历\"\"\"\n    if not root:\n        return []\n    return postorder(root.left) + postorder(root.right) + [root.val]\n\ndef tree_height(root):\n    \"\"\"树的高度\"\"\"\n    if not root:\n        return 0\n    return 1 + max(tree_height(root.left), tree_height(root.right))\n\n# 构建树: [1, 2, 3, 4, 5]\n#       1\n#      / \\\n#     2   3\n#    / \\\n#   4   5\ntree = build_tree_from_list([1, 2, 3, 4, 5])\nprint(f\"前序: {preorder(tree)}\")    # [1, 2, 4, 5, 3]\nprint(f\"中序: {inorder(tree)}\")     # [4, 2, 5, 1, 3]\nprint(f\"后序: {postorder(tree)}\")   # [4, 5, 2, 3, 1]\nprint(f\"高度: {tree_height(tree)}\") # 3",
                "exercise": {
                    "description": "实现二叉树的中序遍历。\n输入 n 个整数（用列表构建完全二叉树，None 表示空节点），输出中序遍历结果。\n\n提示：递归方法如前所示",
                    "template": "class TreeNode:\n    def __init__(self, val):\n        self.val = val\n        self.left = None\n        self.right = None\n\ndef build_tree(arr, idx=0):\n    if idx >= len(arr) or arr[idx] is None:\n        return None\n    root = TreeNode(arr[idx])\n    root.left = build_tree(arr, 2*idx+1)\n    root.right = build_tree(arr, 2*idx+2)\n    return root\n\ndef inorder(root):\n    \n\n# 构建树\nvalues = [int(x) if x != 'None' else None for x in input().split()]\nroot = build_tree(values)\nresult = inorder(root)\nprint(' '.join(map(str, result)))",
                    "sample_input": "1 2 3 4 5",
                    "sample_output": "4 2 5 1 3"
                }
            }
        ]
    },

    # ============================================================
    # 第13阶段：大型综合项目
    # ============================================================
    {
        "id": 45,
        "name": "项目实战 - 命令行工具",
        "phase": "第13阶段：大型综合项目",
        "steps": [
            {
                "concept": "用Python开发一个完整的命令行待办事项管理器（Todo CLI）。\n\n功能要求：\n1. 添加任务（add）\n2. 查看所有任务（list）\n3. 完成任务（done）\n4. 删除任务（delete）\n5. 保存到JSON文件（持久化）\n\n涉及知识点：\n• 文件操作（json）\n• 命令行参数（sys.argv）\n• 列表操作\n• 日期处理（datetime）\n• 异常处理",
                "example": "import json\nimport sys\nfrom datetime import datetime\n\nTODO_FILE = \"todo.json\"\n\ndef load_tasks():\n    try:\n        with open(TODO_FILE, \"r\") as f:\n            return json.load(f)\n    except (FileNotFoundError, json.JSONDecodeError):\n        return []\n\ndef save_tasks(tasks):\n    with open(TODO_FILE, \"w\") as f:\n        json.dump(tasks, f, ensure_ascii=False, indent=2)\n\ndef add_task(description):\n    tasks = load_tasks()\n    task = {\n        \"id\": len(tasks) + 1,\n        \"description\": description,\n        \"done\": False,\n        \"created_at\": datetime.now().isoformat()\n    }\n    tasks.append(task)\n    save_tasks(tasks)\n    print(f\"✅ 已添加: {description}\")\n\ndef list_tasks():\n    tasks = load_tasks()\n    if not tasks:\n        print(\"📭 暂无任务\")\n        return\n    print(\"\\n📋 待办事项:\")\n    for task in tasks:\n        status = \"✅\" if task[\"done\"] else \"⬜\"\n        print(f\"  {status} [{task['id']}] {task['description']}\")\n\ndef done_task(task_id):\n    tasks = load_tasks()\n    for task in tasks:\n        if task[\"id\"] == task_id:\n            task[\"done\"] = True\n            save_tasks(tasks)\n            print(f\"✅ 已完成: {task['description']}\")\n            return\n    print(f\"❌ 未找到ID: {task_id}\")\n\nif __name__ == \"__main__\":\n    if len(sys.argv) < 2:\n        print(\"用法: python todo.py <命令> [参数]\")\n        print(\"命令: add, list, done\")\n        sys.exit(1)\n    \n    cmd = sys.argv[1]\n    if cmd == \"add\" and len(sys.argv) > 2:\n        add_task(sys.argv[2])\n    elif cmd == \"list\":\n        list_tasks()\n    elif cmd == \"done\" and len(sys.argv) > 2:\n        done_task(int(sys.argv[2]))\n    else:\n        print(\"未知命令\")",
                "exercise": {
                    "description": "本课为项目实战课，请在本地创建 todo.py 文件，实现待办事项管理器。\n完成后测试：\n1. python todo.py add \"学习Python\"\n2. python todo.py list\n3. python todo.py done 1\n\n此处直接输出\"项目创建成功\"即可。",
                    "template": "print(\"项目创建成功\")\nprint(\"请在本地运行: python todo.py list\")",
                    "sample_input": "",
                    "sample_output": "项目创建成功\n请在本地运行: python todo.py list"
                }
            }
        ]
    },
    {
        "id": 46,
        "name": "项目实战 - 数据可视化",
        "phase": "第13阶段：大型综合项目",
        "steps": [
            {
                "concept": "用 matplotlib 进行数据可视化。\n\n安装：pip install matplotlib\n\n常用图表：\n  import matplotlib.pyplot as plt\n  \n  plt.plot(x, y)         - 折线图\n  plt.bar(x, y)          - 柱状图\n  plt.scatter(x, y)      - 散点图\n  plt.pie(values)        - 饼图\n  plt.hist(data)         - 直方图\n  plt.boxplot(data)      - 箱线图\n\n美化：\n  plt.title()  plt.xlabel()  plt.ylabel()\n  plt.grid()   plt.legend()\n  plt.savefig('chart.png')",
                "example": "# 在本地运行这段代码\nimport matplotlib.pyplot as plt\nimport numpy as np\n\n# 生成数据\nx = np.linspace(0, 10, 100)\ny1 = np.sin(x)\ny2 = np.cos(x)\n\n# 创建图表\nplt.figure(figsize=(10, 6))\n\nplt.plot(x, y1, label='sin(x)', linewidth=2, color='blue')\nplt.plot(x, y2, label='cos(x)', linewidth=2, color='red')\n\nplt.title('正弦和余弦函数', fontsize=14)\nplt.xlabel('x', fontsize=12)\nplt.ylabel('y', fontsize=12)\nplt.grid(True, alpha=0.3)\nplt.legend()\n\nplt.savefig('trig_functions.png', dpi=150)\nplt.show()\n\nprint(\"图表已保存为 trig_functions.png\")",
                "exercise": {
                    "description": "数据可视化为理解题，请在本地安装 matplotlib 后运行示例代码。\n\n本题直接输出\"图表已生成\"。",
                    "template": "print(\"图表已生成\")\nprint(\"请在本地运行可视化代码\")",
                    "sample_input": "",
                    "sample_output": "图表已生成\n请在本地运行可视化代码"
                }
            }
        ]
    }
]

PHASES_PYTHON_V3 = [
    "第8阶段：Web开发与网络编程",
    "第9阶段：测试与调试",
    "第10阶段：高级面向对象",
    "第11阶段：性能优化与并发",
    "第12阶段：算法与竞赛实战",
    "第13阶段：大型综合项目"
]
