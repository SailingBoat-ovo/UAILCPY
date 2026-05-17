# -*- coding: utf-8 -*-
# Python高级课程 - 竞赛级内容

lessons_python_advanced = [
    {
        "id": 25,
        "name": "高阶函数与functools",
        "phase": "第7阶段：Python进阶与竞赛",
        "steps": [
            {
                "concept": "functools 模块提供了高阶函数工具，在竞赛中非常实用。\n\npartial：固定部分参数\n  from functools import partial\n  def pow(base, exp): return base ** exp\n  square = partial(pow, exp=2)\n  cube = partial(pow, exp=3)\n  print(square(5), cube(5))  # 25 125\n\nlru_cache：自动记忆化（缓存函数结果）\n  @lru_cache(maxsize=None)\n  def fib(n):\n      if n < 2: return n\n      return fib(n-1) + fib(n-2)\n  # 瞬间计算 fib(100)\n\nwraps：装饰器传递函数元信息",
                "example": "from functools import partial, lru_cache, wraps\n\n# partial\nint_base2 = partial(int, base=2)\nprint(int_base2(\"1010\"))  # 10\n\n# lru_cache\n@lru_cache(maxsize=None)\ndef fib(n):\n    if n <= 1:\n        return n\n    return fib(n-1) + fib(n-2)\n\nprint(fib(50))  # 12586269025（瞬间出结果）\nprint(fib.cache_info())  # CacheInfo(hits=48, misses=51, ...)\n\n# wraps\nfrom functools import wraps\ndef my_decorator(f):\n    @wraps(f)\n    def wrapper(*args, **kwargs):\n        \"\"\"wrapper doc\"\"\"\n        return f(*args, **kwargs)\n    return wrapper\n\n@my_decorator\ndef example():\n    \"\"\"example doc\"\"\"\n    pass\n\nprint(example.__name__)  # example（没有wraps会输出wrapper）\nprint(example.__doc__)   # example doc",
                "exercise": {
                    "description": "用 @lru_cache 加速递归计算斐波那契数列第 n 项。\n输入 n（n <= 100），输出 fib(n) % 1000000007。\n\n输入：50\n输出：365010934\n\n提示：取模防止数字过大",
                    "template": "from functools import lru_cache\n\n@lru_cache(maxsize=None)\ndef fib(n):\n    if n <= 1:\n        return n\n    return (fib(n-1) + fib(n-2)) % 1000000007\n\nn = int(input())\nprint(fib(n))",
                    "sample_input": "50",
                    "sample_output": "365010934"
                }
            },
            {
                "concept": "singledispatch：单分派泛型函数\n根据第一个参数的类型执行不同的函数。\n\n  from functools import singledispatch\n  \n  @singledispatch\n  def process(arg):\n      return f\"默认：{arg}\"\n  \n  @process.register(int)\n  def _(arg):\n      return f\"整数：{arg}\"\n  \n  @process.register(list)\n  def _(arg):\n      return f\"列表，长度{len(arg)}：{arg}\"\n\nreduce：累积计算（Python 3 在 functools 中）\n  from functools import reduce\n  reduce(lambda a, b: a * b, [1, 2, 3, 4, 5])  # 120",
                "example": "from functools import singledispatch, reduce\n\n@singledispatch\ndef describe(obj):\n    return f\"未知类型: {type(obj).__name__}\"\n\n@describe.register(int)\ndef _(obj):\n    if obj % 2 == 0:\n        return f\"偶数: {obj}\"\n    return f\"奇数: {obj}\"\n\n@describe.register(str)\ndef _(obj):\n    return f\"字符串 ({len(obj)}字符): {obj}\"\n\n@describe.register(list)\ndef _(obj):\n    return f\"列表 {len(obj)}个元素: 最大={max(obj)}, 最小={min(obj)}\"\n\nprint(describe(42))\nprint(describe(\"Hello\"))\nprint(describe([3, 1, 4, 1, 5]))\n\n# reduce\nnums = [1, 2, 3, 4, 5]\nproduct = reduce(lambda x, y: x * y, nums)\nprint(f\"连乘: {product}\")  # 120",
                "exercise": {
                    "description": "用 singledispatch 实现一个函数 process_data，对不同类型的参数返回不同结果：\n- int: 返回 \"整数: 值\"\n- str: 返回 \"字符串: 值\"\n- list: 返回列表元素的和\n- 其他: 返回 \"未知类型\"\n\n输入：一个整数\n输出：整数: 42",
                    "template": "from functools import singledispatch\n\n@singledispatch\ndef process_data(arg):\n    return \"未知类型\"\n\n\n\nprint(process_data(int(input())))",
                    "sample_input": "42",
                    "sample_output": "整数: 42"
                }
            }
        ]
    },
    {
        "id": 26,
        "name": "上下文管理器 - with语句",
        "phase": "第7阶段：Python进阶与竞赛",
        "steps": [
            {
                "concept": "上下文管理器 = with 语句，自动管理资源的获取和释放。\n\n实现方式一：类 + __enter__ / __exit__\n  class MyContext:\n      def __enter__(self):\n          print(\"进入\")\n          return self\n      def __exit__(self, *args):\n          print(\"退出\")\n\n实现方式二：@contextmanager 装饰器\n  from contextlib import contextmanager\n  \n  @contextmanager\n  def my_context():\n      print(\"进入\")\n      yield\n      print(\"退出\")\n\n即使在 with 块中发生异常，__exit__ 也会被执行。",
                "example": "from contextlib import contextmanager\n\n# 用装饰器实现\n@contextmanager\ndef timed(name):\n    import time\n    start = time.time()\n    print(f\"[{name}] 开始\")\n    yield\n    elapsed = time.time() - start\n    print(f\"[{name}] 耗时: {elapsed:.4f}秒\")\n\n# 使用\nwith timed(\"计算\"):\n    result = sum(range(1000000))\n    print(f\"结果: {result}\")\n\n# 文件操作本身就是上下文管理器\nwith open(\"test.txt\", \"w\") as f:\n    f.write(\"自动关闭！\")\n\n# 管理多个资源\nwith open(\"a.txt\", \"w\") as a, open(\"b.txt\", \"w\") as b:\n    a.write(\"file a\")\n    b.write(\"file b\")",
                "exercise": {
                    "description": "用 @contextmanager 实现一个 cd 上下文管理器，临时改变当前工作目录，退出时恢复。\n\n提示：os.getcwd() 获取当前目录，os.chdir() 切换目录\nimport os\nfrom contextlib import contextmanager\n\n测试：先输出当前目录，然后进入父目录，再退出。",
                    "template": "import os\nfrom contextlib import contextmanager\n\n@contextmanager\ndef change_dir(path):\n    \n\n# 测试\nprint(\"当前:\", os.getcwd())\nwith change_dir(\"..\"):\n    print(\"进入:\", os.getcwd())\nprint(\"恢复:\", os.getcwd())\n",
                    "sample_input": "",
                    "sample_output": "当前: ...\n进入: ...\n恢复: ..."
                }
            }
        ]
    },
    {
        "id": 27,
        "name": "itertools - 迭代器工具",
        "phase": "第7阶段：Python进阶与竞赛",
        "steps": [
            {
                "concept": "itertools 是竞赛中极其有用的模块，提供高效的迭代器工具。\n\n常用函数：\n  count(start, step)    - 无限计数\n  cycle(iterable)       - 无限循环\n  repeat(x, n)          - 重复n次\n  \n  chain(a, b, c)        - 连接多个可迭代对象\n  chain.from_iterable() - 展平嵌套\n  \n  product(a, b)         - 笛卡尔积（n重循环）\n  permutations(a, n)    - 排列\n  combinations(a, n)    - 组合\n  combinations_with_replacement(a, n) - 可重复组合\n  \n  groupby(iterable, key) - 分组\n  accumulate(iterable)   - 累积（前缀和）",
                "example": "from itertools import *\n\n# 排列组合（竞赛高频考点）\nitems = [1, 2, 3]\n\nprint(\"排列 P(3,2):\")\nfor p in permutations(items, 2):\n    print(p, end=\" \")  # (1,2) (1,3) (2,1) (2,3) (3,1) (3,2)\nprint()\n\nprint(\"组合 C(3,2):\")\nfor c in combinations(items, 2):\n    print(c, end=\" \")  # (1,2) (1,3) (2,3)\nprint()\n\nprint(\"笛卡尔积:\")\nfor p in product([1, 2], \"AB\"):\n    print(p, end=\" \")  # (1,'A') (1,'B') (2,'A') (2,'B')\nprint()\n\n# 前缀和\nfrom itertools import accumulate\nnums = [1, 2, 3, 4, 5]\nprefix = list(accumulate(nums))\nprint(f\"前缀和: {prefix}\")  # [1, 3, 6, 10, 15]",
                "exercise": {
                    "description": "输入 n 和 k，输出从 1 到 n 中选 k 个数的所有组合。\n每行一个组合，数字空格隔开。\n\n输入：4 2\n输出：\n1 2\n1 3\n1 4\n2 3\n2 4\n3 4\n\n提示：from itertools import combinations",
                    "template": "from itertools import combinations\n\nn, k = map(int, input().split())\n\n",
                    "sample_input": "4 2",
                    "sample_output": "1 2\n1 3\n1 4\n2 3\n2 4\n3 4"
                }
            }
        ]
    },
    {
        "id": 28,
        "name": "正则表达式 - 文本处理利器",
        "phase": "第7阶段：Python进阶与竞赛",
        "steps": [
            {
                "concept": "正则表达式 = 一种文本模式匹配语言。\n需要 import re\n\n常用函数：\n  re.search(pattern, s)   - 搜索第一个匹配\n  re.findall(pattern, s)  - 找到所有匹配\n  re.sub(pattern, rep, s) - 替换\n  re.split(pattern, s)    - 分割\n  re.match(pattern, s)    - 从开头匹配\n\n常用模式：\n  \\d   数字      \\w   字母数字下划线\n  \\s   空白      .    任意字符（除换行）\n  *    0次或多次  +    1次或多次\n  ?    0次或1次   {n}  精确n次\n  ^    开头      $    结尾\n  []   字符集     ()   分组",
                "example": "import re\n\ntext = \"联系方式: 张三 138-1234-5678, 李四 139-4321-8765\"\n\n# 提取所有电话号码\nphones = re.findall(r'\\d{3}-\\d{4}-\\d{4}', text)\nprint(f\"电话: {phones}\")\n\n# 验证邮箱格式\nemail = \"test@example.com\"\npattern = r'^[\\w.-]+@[\\w.-]+\\.\\w+$'\nif re.match(pattern, email):\n    print(\"邮箱格式正确\")\n\n# 替换\nresult = re.sub(r'\\d{3}-\\d{4}-\\d{4}', '***-****-****', text)\nprint(f\"脱敏: {result}\")\n\n# 分割\ns = \"a,b;c|d\"\nparts = re.split(r'[,;|]', s)\nprint(f\"分割: {parts}\")",
                "exercise": {
                    "description": "输入一行文本，用正则表达式提取其中所有的整数（可能包含负数）。\n输出所有整数之和。\n\n输入：abc -5 def 10 ghi 20 jkl -3\n输出：22\n\n提示：re.findall(r'-?\\d+', text) 然后 map(int, ...)",
                    "template": "import re\n\ntext = input()\n",
                    "sample_input": "abc -5 def 10 ghi 20 jkl -3",
                    "sample_output": "22"
                }
            }
        ]
    },
    {
        "id": 29,
        "name": "asyncio - 异步编程",
        "phase": "第7阶段：Python进阶与竞赛",
        "steps": [
            {
                "concept": "asyncio 是 Python 的异步 I/O 框架，用于并发执行 I/O 操作。\n\n核心概念：\n  async def    - 定义协程\n  await        - 等待协程完成\n  asyncio.run() - 运行主协程\n  asyncio.gather() - 并发执行多个协程\n\n和线程的区别：\n- 线程：操作系统调度，适合CPU密集型\n- 协程：单线程内协作式调度，适合I/O密集型\n\n异步编程适合：网络请求、文件读写、数据库操作等。",
                "example": "import asyncio\n\nasync def fetch_data(name, delay):\n    print(f\"[{name}] 开始获取...\")\n    await asyncio.sleep(delay)  # 模拟 I/O 操作\n    print(f\"[{name}] 完成！（耗时{delay}秒）\")\n    return f\"{name}的数据\"\n\nasync def main():\n    # 顺序执行\n    result1 = await fetch_data(\"A\", 2)\n    \n    # 并发执行\n    results = await asyncio.gather(\n        fetch_data(\"B\", 1),\n        fetch_data(\"C\", 3),\n        fetch_data(\"D\", 2)\n    )\n    print(f\"所有结果: {results}\")\n\n# 运行\n# asyncio.run(main())\n\nprint(\"异步编程要点：\")\nprint(\"1. async def 定义协程\")\nprint(\"2. await 等待协程\")\nprint(\"3. gather 并发执行\")\nprint(\"4. 协程适合 I/O 密集型任务\")",
                "exercise": {
                    "description": "由于评测环境限制，这里改为理解题。\n请编写一个异步函数 delayed_print(msg, delay)，实现延迟打印。\n\n然后创建两个并发任务分别延迟1秒和2秒打印不同消息。\n\n（在实际环境中运行）",
                    "template": "import asyncio\n\nasync def delayed_print(msg, delay):\n    \n\nasync def main():\n    \n\n# asyncio.run(main())",
                    "sample_input": "",
                    "sample_output": "Hello\nWorld"
                }
            }
        ]
    },
    {
        "id": 30,
        "name": "算法 - 排序与搜索",
        "phase": "第7阶段：Python进阶与竞赛",
        "steps": [
            {
                "concept": "竞赛必备算法：排序、二分搜索、双指针。\n\nPython 内置排序 Timsort O(n log n)：\n  sorted(list)          - 返回新列表\n  list.sort()           - 原地排序\n  sorted(list, key=fn)  - 自定义排序键\n  sorted(list, reverse=True) - 降序\n\n二分搜索（需要已排序数组）：\n  import bisect\n  bisect.bisect_left(arr, x)  - 第一个 >= x 的位置\n  bisect.bisect_right(arr, x) - 第一个 > x 的位置\n  bisect.insort(arr, x)       - 插入并保持有序\n\n双指针技巧：\n  左右指针向中间移动，用于有序数组的查找。",
                "example": "import bisect\n\n# 二分搜索\narr = [1, 3, 5, 7, 9, 11]\ntarget = 7\n\npos = bisect.bisect_left(arr, target)\nif pos < len(arr) and arr[pos] == target:\n    print(f\"找到 {target}，位置 {pos}\")\nelse:\n    print(f\"没找到，应插入位置 {pos}\")\n\n# 双指针：两数之和 II（已排序）\ndef two_sum(nums, target):\n    left, right = 0, len(nums) - 1\n    while left < right:\n        s = nums[left] + nums[right]\n        if s == target:\n            return [left, right]\n        elif s < target:\n            left += 1\n        else:\n            right -= 1\n    return []\n\narr = [2, 7, 11, 15]\nprint(f\"两数之和: {two_sum(arr, 9)}\")  # [0, 1]\n\n# 自定义排序\nstudents = [(\"张三\", 85), (\"李四\", 92), (\"王五\", 78)]\nsorted_stu = sorted(students, key=lambda x: x[1], reverse=True)\nprint(f\"按成绩排序: {sorted_stu}\")",
                "exercise": {
                    "description": "输入一个已排序的数组和目标值，用 bisect 找到目标值的第一个和最后一个出现位置。\n如果没找到输出 \"-1 -1\"。\n\n输入：\n1 2 2 2 3 4 5\n2\n输出：1 3\n\n提示：bisect_left 和 bisect_right",
                    "template": "import bisect\n\narr = list(map(int, input().split()))\ntarget = int(input())\n\nleft = bisect.bisect_left(arr, target)\nright = bisect.bisect_right(arr, target) - 1\n",
                    "sample_input": "1 2 2 2 3 4 5\n2",
                    "sample_output": "1 3"
                }
            }
        ]
    },
    {
        "id": 31,
        "name": "数据结构 - collections模块",
        "phase": "第7阶段：Python进阶与竞赛",
        "steps": [
            {
                "concept": "collections 模块提供高效的数据结构，竞赛必用。\n\nCounter：计数器\n  from collections import Counter\n  c = Counter(\"abracadabra\")\n  print(c.most_common(3))  # [('a',5), ('b',2), ('r',2)]\n\ndefaultdict：带默认值的字典\n  d = defaultdict(list)\n  d['key'].append(1)  # 不需要先初始化\n\ndeque：双端队列（高效的头尾操作）\n  from collections import deque\n  dq = deque([1, 2, 3])\n  dq.appendleft(0)  # O(1)\n  dq.pop()          # O(1)\n  dq.popleft()      # O(1)\n\nnamedtuple：命名元组\n  Point = namedtuple('Point', ['x', 'y'])\n  p = Point(3, 4)\n  print(p.x, p.y)",
                "example": "from collections import Counter, defaultdict, deque, namedtuple\n\n# Counter 统计频率\ntext = \"mississippi\"\ncounter = Counter(text)\nprint(f\"字符频率: {counter}\")\nprint(f\"出现最多3个: {counter.most_common(3)}\")\n\n# defaultdict 分组\nstudents = [(\"A\", 85), (\"B\", 92), (\"A\", 78), (\"B\", 88)]\ngroups = defaultdict(list)\nfor name, score in students:\n    groups[name].append(score)\nprint(f\"分组: {dict(groups)}\")\n\n# deque 滑动窗口\nfrom itertools import accumulate\ndef max_sliding_window(nums, k):\n    dq = deque()\n    result = []\n    for i, v in enumerate(nums):\n        while dq and nums[dq[-1]] < v:\n            dq.pop()\n        dq.append(i)\n        if dq[0] <= i - k:\n            dq.popleft()\n        if i >= k - 1:\n            result.append(nums[dq[0]])\n    return result\n\nnums = [1, 3, -1, -3, 5, 3, 6, 7]\nprint(f\"滑动窗口最大值: {max_sliding_window(nums, 3)}\")\n# [3, 3, 5, 5, 6, 7]\n\n# namedtuple\nPoint = namedtuple('Point', ['x', 'y'])\np = Point(3, 4)\nprint(f\"距离: {(p.x**2 + p.y**2)**0.5:.2f}\")",
                "exercise": {
                    "description": "输入一行单词，用 Counter 统计每个单词出现的次数。\n按出现次数从高到低输出（次数相同按单词字典序）。\n\n输入：apple banana apple orange banana apple\n输出：\napple: 3\nbanana: 2\norange: 1",
                    "template": "from collections import Counter\n\nwords = input().split()\n",
                    "sample_input": "apple banana apple orange banana apple",
                    "sample_output": "apple: 3\nbanana: 2\norange: 1"
                }
            }
        ]
    }
]

PHASES_PYTHON_ADVANCED = ["第7阶段：Python进阶与竞赛"]
