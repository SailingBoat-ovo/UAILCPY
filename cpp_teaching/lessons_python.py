# -*- coding: utf-8 -*-

lessons_python = [

    # ============================================================
    # 第1阶段：Python基础入门 (0-4课)
    # ============================================================
    {
        "id": 0,
        "name": "第一行代码 - print输出",
        "phase": "第1阶段：Python基础入门",
        "steps": [
            {
                "concept": "print() 是Python最基本的输出函数，用来在屏幕上显示文字。\n字符串需要用引号括起来，单引号 ' 或双引号 \" 都可以。\n\nPython的特点：\n• 不需要分号结尾\n• 不需要写main函数\n• 缩进表示代码块（重要！）\n• 大小写敏感（print和Print不同）",
                "example": "print(\"Hello, World!\")\nprint('Python is fun')",
                "exercise": {
                    "description": "用 print() 输出你的名字（可以输出任意名字）",
                    "template": "",
                    "sample_input": "",
                    "sample_output": "小明"
                }
            },
            {
                "concept": "一个 print() 输出一行。要输出多行内容，可以用多个 print()。\n\nprint() 也可以不输出任何内容，就做一个空行。",
                "example": "print(\"第一行\")\nprint()  # 空行\nprint(\"第三行\")",
                "exercise": {
                    "description": "分两行输出以下内容：\n第一行：I love Python\n第二行：Hello World",
                    "template": "",
                    "sample_input": "",
                    "sample_output": "I love Python\nHello World"
                }
            },
            {
                "concept": "print() 可以同时输出多个内容，用逗号隔开，会自动加空格。\nprint() 的 end 参数可以指定结尾字符，默认是 \\n（换行）。",
                "example": "print(\"苹果\", \"香蕉\", \"橘子\")\nprint(1, 2, 3, sep=\"-\")\nprint(\"Hello\", end=\"\")\nprint(\" World\")",
                "exercise": {
                    "description": "用 print 输出：2024 年 12 月 25 日\n（用逗号隔开，中间有空格）",
                    "template": "",
                    "sample_input": "",
                    "sample_output": "2024 年 12 月 25 日"
                }
            }
        ]
    },
    {
        "id": 1,
        "name": "变量 - 数据的容器",
        "phase": "第1阶段：Python基础入门",
        "steps": [
            {
                "concept": "变量就像贴了标签的盒子，用来存储数据。\nPython不需要声明类型，直接赋值即可：\n  变量名 = 值\n\n变量命名规则：\n• 字母、数字、下划线组成\n• 不能以数字开头\n• 不能是Python关键字（if、for、while等）\n• 区分大小写（name和Name不同）\n• 要见名知意！",
                "example": "name = \"小明\"\nage = 18\nprint(name)\nprint(age)",
                "exercise": {
                    "description": "创建一个变量 score，赋值为100，然后输出它。",
                    "template": "",
                    "sample_input": "",
                    "sample_output": "100"
                }
            },
            {
                "concept": "Python常见数据类型：\n  int    - 整数（1, 100, -5）\n  float  - 浮点数/小数（3.14, -0.5）\n  str    - 字符串（\"Hello\"）\n  bool   - 布尔值（True / False）\n  NoneType - 空值（None）\n\n用 type() 函数可以查看变量的类型。",
                "example": "x = 10\nprint(type(x))  # <class 'int'>\ny = 3.14\nprint(type(y))  # <class 'float'>\nz = \"Hi\"\nprint(type(z))  # <class 'str'>\nb = True\nprint(type(b))  # <class 'bool'>",
                "exercise": {
                    "description": "创建三个变量：\n  a = 5（整数）\n  b = 2.5（小数）\n  c = \"Hello\"（字符串）\n输出 a + b 的结果。",
                    "template": "",
                    "sample_input": "",
                    "sample_output": "7.5"
                }
            },
            {
                "concept": "同时给多个变量赋值：\n  a, b, c = 1, 2, 3\n  a = b = c = 0  （都赋值为0）\n\n交换两个变量的值非常方便：\n  a, b = b, a",
                "example": "a, b, c = 10, 20, 30\nprint(a, b, c)\n\na, b = b, a\nprint(\"交换后:\", a, b)",
                "exercise": {
                    "description": "输入两个整数 a 和 b，交换它们的值后输出。\n\n输入：3 5\n输出：5 3",
                    "template": "a, b = map(int, input().split())\n",
                    "sample_input": "3 5",
                    "sample_output": "5 3"
                }
            }
        ]
    },
    {
        "id": 2,
        "name": "输入与格式化输出",
        "phase": "第1阶段：Python基础入门",
        "steps": [
            {
                "concept": "input() 从键盘获取用户输入，返回的是字符串。\n可以带提示文字：input(\"请输入：\")\n\n如果需要数字，要用类型转换：\n  int(input())    → 整数\n  float(input())  → 小数\n\n多个输入用 split() 分割：\n  a, b = input().split()  → 得到两个字符串\n  a, b = map(int, input().split())  → 得到两个整数",
                "example": "name = input(\"你的名字：\")\nprint(\"你好，\" + name + \"！\")\n\nage = int(input(\"年龄：\"))\nprint(\"明年你\", age + 1, \"岁\")",
                "exercise": {
                    "description": "编写程序：\n1. 提示输入名字\n2. 读取名字\n3. 输出\"欢迎你，[名字]！\"",
                    "template": "",
                    "sample_input": "小红",
                    "sample_output": "欢迎你，小红！"
                }
            },
            {
                "concept": "f-string 格式化（Python 3.6+ 推荐使用）：\n  name = \"小明\"\n  print(f\"你好，{name}\")\n\n在花括号 { } 中可以直接放变量或表达式。\n可以指定格式：\n  {变量:.2f}  → 保留2位小数\n  {变量:>5}   → 右对齐，宽度5",
                "example": "name = \"小明\"\nage = 18\nprint(f\"我叫{name}，今年{age}岁\")\nprint(f\"明年{age+1}岁\")\n\npi = 3.1415926\nprint(f\"圆周率：{pi:.2f}\")",
                "exercise": {
                    "description": "输入半径 r，用 f-string 输出圆的周长和面积。\n周长 = 2 * 3.14 * r\n面积 = 3.14 * r * r\n结果保留2位小数。\n\n输出格式：\"周长：xx.xx\" 换行 \"面积：xx.xx\"",
                    "template": "",
                    "sample_input": "5",
                    "sample_output": "周长：31.40\n面积：78.50"
                }
            },
            {
                "concept": "字符串拼接方式总结：\n1. + 号拼接：\"Hello\" + \" \" + \"World\"\n2. f-string：f\"{变量}\" （最推荐）\n3. format()：\"{} {}\".format(a, b)\n4. % 格式化：\"%s %d\" % (name, age)",
                "example": "name = \"小明\"\nscore = 95\n\n# 四种方式效果相同\nprint(\"姓名：\" + name + \"，成绩：\" + str(score))\nprint(f\"姓名：{name}，成绩：{score}\")   # 推荐\nprint(\"姓名：{}，成绩：{}\".format(name, score))\nprint(\"姓名：%s，成绩：%d\" % (name, score))",
                "exercise": {
                    "description": "输入姓名和成绩（用空格隔开），用 f-string 输出：\n\"学生：张三，成绩：95分\"",
                    "template": "name, score = input().split()\n",
                    "sample_input": "张三 95",
                    "sample_output": "学生：张三，成绩：95分"
                }
            }
        ]
    },
    {
        "id": 3,
        "name": "运算符 - 让Python做计算",
        "phase": "第1阶段：Python基础入门",
        "steps": [
            {
                "concept": "算术运算符：\n  +   加法      -   减法\n  *   乘法      /   除法（结果总是小数！）\n  //  整除      %   取余\n  **  幂运算\n\n注意：Python 的 / 和 C++ 不同，5/2 = 2.5 不是 2！\n整数除法要用 //：5//2 = 2",
                "example": "a, b = 10, 3\nprint(a + b)   # 13\nprint(a - b)   # 7\nprint(a * b)   # 30\nprint(a / b)   # 3.333...（小数）\nprint(a // b)  # 3（整除）\nprint(a % b)   # 1（余数）\nprint(a ** b)  # 1000（10的3次方）",
                "exercise": {
                    "description": "输入两个整数 a 和 b，输出它们的和、差、积、商（整除）、余数。\n每行一个结果。",
                    "template": "",
                    "sample_input": "17 5",
                    "sample_output": "22\n12\n85\n3\n2"
                }
            },
            {
                "concept": "复合赋值运算符：\n  +=   a += 1  等价于 a = a + 1\n  -=   a -= 1  等价于 a = a - 1\n  *=   a *= 2  等价于 a = a * 2\n  /=   a /= 2  等价于 a = a / 2\n  //=  a //= 2\n  %=   a %= 2\n  **=  a **= 2\n\n自增自减：Python 没有 i++！要用 i += 1",
                "example": "x = 10\nx += 5   # x = 15\nx *= 2   # x = 30\nx //= 4  # x = 7\nprint(x)\n\ny = 2\ny **= 10  # y = 1024\nprint(y)",
                "exercise": {
                    "description": "输入一个整数 n，输出它的平方、立方和2的n次方。\n\n提示：n**2, n**3, 2**n",
                    "template": "",
                    "sample_input": "5",
                    "sample_output": "25\n125\n32"
                }
            },
            {
                "concept": "比较运算符（结果都是 bool 类型）：\n  ==  等于    !=  不等于\n  >   大于    <   小于\n  >=  大于等于  <=  小于等于\n\n逻辑运算符：\n  and  与（两边都真才真）\n  or   或（一边真就真）\n  not  非（取反）\n\n短路特性：and 左边为假就不算右边；or 左边为真就不算右边。",
                "example": "x, y = 5, 10\nprint(x == y)   # False\nprint(x < y)    # True\nprint(x > 0 and y < 20)  # True\nprint(x > 0 or y > 20)   # True\nprint(not (x > y))       # True",
                "exercise": {
                    "description": "输入三个整数 a, b, c，判断 a 是否等于 b+c。\n是输出\"Yes\"，否则输出\"No\"。",
                    "template": "",
                    "sample_input": "10 4 6",
                    "sample_output": "Yes"
                }
            }
        ]
    },
    {
        "id": 4,
        "name": "类型转换与常用函数",
        "phase": "第1阶段：Python基础入门",
        "steps": [
            {
                "concept": "常见类型转换函数：\n  int(x)    → 转为整数\n  float(x)  → 转为小数\n  str(x)    → 转为字符串\n  bool(x)   → 转为布尔值\n  list(x)   → 转为列表\n\n注意：int(\"3.14\") 会报错！要先 float 再 int。\nbool 转换规则：0、\"\"、[]、None 为 False，其他为 True。",
                "example": "print(int(3.99))     # 3（直接截断，不是四舍五入）\nprint(float(\"3.14\")) # 3.14\nprint(str(100))       # \"100\"\nprint(bool(0))        # False\nprint(bool(1))        # True\nprint(bool(\"\"))      # False\nprint(bool(\" \"))    # True",
                "exercise": {
                    "description": "输入一个小数，输出它的整数部分（用 int 转换）和小数部分（原数减整数部分）。\n保留2位小数。\n\n输入：3.14159\n输出：3\n0.14",
                    "template": "",
                    "sample_input": "3.14159",
                    "sample_output": "3\n0.14"
                }
            },
            {
                "concept": "Python常用内置函数：\n  abs(x)    → 绝对值\n  max(a,b)  → 最大值\n  min(a,b)  → 最小值\n  sum(list) → 求和\n  round(x,n)→ 四舍五入\n  len(s)    → 长度\n  range(n)  → 生成0到n-1的序列\n  ord(c)    → 字符转ASCII码\n  chr(n)    → ASCII码转字符",
                "example": "print(abs(-5))       # 5\nprint(max(3, 7, 1))  # 7\nprint(min(3, 7, 1))  # 1\nprint(round(3.14159, 2))  # 3.14\nprint(ord('A'))      # 65\nprint(chr(65))       # 'A'",
                "exercise": {
                    "description": "输入两个整数 a 和 b，输出它们的绝对值之和、最大值和最小值。\n\n输入：-5 8\n输出：13\n8\n-5",
                    "template": "",
                    "sample_input": "-5 8",
                    "sample_output": "13\n8\n-5"
                }
            }
        ]
    },

    # ============================================================
    # 第2阶段：控制流程 (5-9课)
    # ============================================================
    {
        "id": 5,
        "name": "条件判断 - if/elif/else",
        "phase": "第2阶段：控制流程",
        "steps": [
            {
                "concept": "if 语句让程序根据条件执行不同代码：\n\n  if 条件:\n      代码块1\n  else:\n      代码块2\n\n重点：\n• 条件后面有冒号 :\n• 代码块需要缩进（通常4个空格）\n• 不要忘记冒号！\n• if 和 else 对齐",
                "example": "score = 85\nif score >= 60:\n    print(\"及格了！\")\nelse:\n    print(\"不及格...\")",
                "exercise": {
                    "description": "输入一个整数，判断奇偶数。\n偶数输出\"偶数\"，奇数输出\"奇数\"。\n\n提示：x % 2 == 0 是偶数",
                    "template": "",
                    "sample_input": "7",
                    "sample_output": "奇数"
                }
            },
            {
                "concept": "多分支用 elif（就是 else if 的缩写）：\n\n  if 条件1:\n      ...\n  elif 条件2:\n      ...\n  elif 条件3:\n      ...\n  else:\n      ...\n\n注意：Python 没有 else if，只有 elif！\n条件是从上到下依次判断，碰到第一个为真的就执行。",
                "example": "score = int(input())\nif score >= 90:\n    print(\"优秀\")\nelif score >= 80:\n    print(\"良好\")\nelif score >= 60:\n    print(\"及格\")\nelse:\n    print(\"不及格\")",
                "exercise": {
                    "description": "输入月份（1-12），输出季节：\n3-5月 → \"春季\"\n6-8月 → \"夏季\"\n9-11月 → \"秋季\"\n12-2月 → \"冬季\"",
                    "template": "",
                    "sample_input": "4",
                    "sample_output": "春季"
                }
            },
            {
                "concept": "嵌套 if：if 里面再套 if。\n\n三目运算符（条件表达式）：\n  x if 条件 else y\n  如果条件为真返回 x，否则返回 y。\n\n例子：\n  result = \"及格\" if score >= 60 else \"不及格\"",
                "example": "age = int(input())\nif age >= 18:\n    if age >= 60:\n        print(\"老年人\")\n    else:\n        print(\"成年人\")\nelse:\n    print(\"未成年人\")\n\n# 三目运算符示例\nx = 5 if age > 10 else 0\nprint(x)",
                "exercise": {
                    "description": "输入三个整数，输出最大的那个数。（用 if/elif/else，不要用 max 函数）",
                    "template": "",
                    "sample_input": "3 7 5",
                    "sample_output": "7"
                }
            }
        ]
    },
    {
        "id": 6,
        "name": "for循环 - 遍历与迭代",
        "phase": "第2阶段：控制流程",
        "steps": [
            {
                "concept": "for 循环用来遍历一个序列（range、字符串、列表等）：\n\n  for 变量 in 序列:\n      循环体\n\nrange(n) → 生成 0 到 n-1\nrange(a, b) → 生成 a 到 b-1\nrange(a, b, c) → 从 a 到 b-1，步长为 c",
                "example": "for i in range(5):\n    print(i, end=\" \")   # 0 1 2 3 4\nprint()\n\nfor i in range(1, 6):\n    print(i, end=\" \")   # 1 2 3 4 5\nprint()\n\nfor i in range(0, 10, 2):\n    print(i, end=\" \")   # 0 2 4 6 8",
                "exercise": {
                    "description": "输入 n，输出 1 到 n 的所有整数，空格隔开。",
                    "template": "",
                    "sample_input": "5",
                    "sample_output": "1 2 3 4 5"
                }
            },
            {
                "concept": "累加求和是循环最常用的操作：\n  1. 定义变量 sum = 0\n  2. 循环中 sum += i\n  3. 循环结束输出 sum\n\n类似的还有累乘求阶乘：\n  fact = 1\n  for i in range(1, n+1):\n      fact *= i",
                "example": "# 1到100求和\nsum = 0\nfor i in range(1, 101):\n    sum += i\nprint(f\"1+2+...+100 = {sum}\")  # 5050\n\n# 求阶乘\nfact = 1\nfor i in range(1, 6):\n    fact *= i\nprint(f\"5! = {fact}\")  # 120",
                "exercise": {
                    "description": "输入 n，计算 1 + 2 + 3 + ... + n 的值。",
                    "template": "",
                    "sample_input": "100",
                    "sample_output": "5050"
                }
            },
            {
                "concept": "嵌套循环：循环里面再套循环。\n外层循环执行一次，内层循环执行一整遍。\n\n常用于打印图案、遍历二维数据等。",
                "example": "# 打印九九乘法表的一部分\nfor i in range(1, 4):\n    for j in range(1, i+1):\n        print(f\"{j}*{i}={i*j}\", end=\" \")\n    print()\n\n# 输出：\n# 1*1=1\n# 1*2=2 2*2=4\n# 1*3=3 2*3=6 3*3=9",
                "exercise": {
                    "description": "输入 n，打印 n 行直角三角形星号图案。\nn=3 时输出：\n*\n**\n***",
                    "template": "",
                    "sample_input": "3",
                    "sample_output": "*\n**\n***"
                }
            }
        ]
    },
    {
        "id": 7,
        "name": "while循环与循环控制",
        "phase": "第2阶段：控制流程",
        "steps": [
            {
                "concept": "while 循环：不知道具体循环次数，只知道终止条件时用。\n\n  while 条件:\n      循环体\n\n和 for 的区别：\n• for：遍历序列（知道要循环多少次）\n• while：满足条件就继续（不知道具体次数）",
                "example": "# 不断输入数字，直到输入0为止\nsum = 0\nnum = int(input())\nwhile num != 0:\n    sum += num\n    num = int(input())\nprint(f\"总和 = {sum}\")",
                "exercise": {
                    "description": "输入一个正整数 n，用 while 循环求它的各位数字之和。\n例如：1234 → 1+2+3+4 = 10\n\n提示：每次取 n%10，然后 n//=10",
                    "template": "",
                    "sample_input": "1234",
                    "sample_output": "10"
                }
            },
            {
                "concept": "break - 立即跳出整个循环。\ncontinue - 跳过本次迭代，进入下一次。\n\nwhile True 是无限循环，必须配合 break 退出。\n\n常见应用：\n• 猜数字游戏\n• 验证输入直到合法\n• 搜索找到就退出",
                "example": "# break：找到第一个能被7整除的三位数\nfor i in range(100, 200):\n    if i % 7 == 0:\n        print(f\"找到了：{i}\")\n        break\n\n# continue：跳过3的倍数\nfor i in range(1, 11):\n    if i % 3 == 0:\n        continue\n    print(i, end=\" \")  # 1 2 4 5 7 8 10",
                "exercise": {
                    "description": "判断素数：输入 n（n>=2），判断是否为素数。\n是输出\"Yes\"，否则输出\"No\"。\n\n素数定义：只能被1和自身整除的数。\n提示：从2到n-1检查有没有能整除的，找到就用 break。",
                    "template": "",
                    "sample_input": "17",
                    "sample_output": "Yes"
                }
            },
            {
                "concept": "else 子句可以接在 for 或 while 后面：\n  for ...:\n      ...\n  else:\n      # 循环正常结束（没被break）时执行\n\n这个特性在其他语言中很少见，可以用来判断循环是否完整执行。",
                "example": "# 检查是否有偶数\nnums = [1, 3, 5, 7, 9]\nfor n in nums:\n    if n % 2 == 0:\n        print(\"找到偶数了\")\n        break\nelse:\n    print(\"没有偶数\")  # 会执行这行",
                "exercise": {
                    "description": "输入一个整数 n，输出它的所有因数（能整除n的数），空格隔开。\n\n例如 n=12，输出：1 2 3 4 6 12",
                    "template": "",
                    "sample_input": "12",
                    "sample_output": "1 2 3 4 6 12"
                }
            }
        ]
    },
    {
        "id": 8,
        "name": "列表 - Python的主力数据结构",
        "phase": "第2阶段：控制流程",
        "steps": [
            {
                "concept": "列表（list）用方括号 [] 表示，可以存放任意类型的元素。\n\n创建列表：\n  lst = [1, 2, 3]\n  lst = []  # 空列表\n  lst = [1, \"hello\", 3.14]  # 混合类型\n\n访问元素：下标从0开始\n  lst[0] → 第一个元素\n  lst[-1] → 最后一个元素\n  lst[-2] → 倒数第二个",
                "example": "nums = [10, 20, 30, 40, 50]\nprint(nums[0])    # 10\nprint(nums[-1])   # 50\nprint(nums[-2])   # 40\n\n# 修改元素\nnums[0] = 100\nprint(nums)  # [100, 20, 30, 40, 50]\n\n# 遍历\nfor i in range(len(nums)):\n    print(nums[i], end=\" \")",
                "exercise": {
                    "description": "输入 n 和 n 个整数，存入列表后输出所有元素的和。",
                    "template": "",
                    "sample_input": "5\n1 2 3 4 5",
                    "sample_output": "15"
                }
            },
            {
                "concept": "列表常用方法：\n  lst.append(x)    - 末尾添加\n  lst.insert(i, x) - 在 i 位置插入\n  lst.remove(x)    - 删除第一个值为 x 的元素\n  lst.pop(i)       - 删除第 i 个元素并返回\n  lst.index(x)     - 查找 x 的位置\n  lst.count(x)     - 统计 x 出现次数\n  lst.sort()       - 排序\n  lst.reverse()    - 反转\n  lst.copy()       - 复制\n  lst.clear()      - 清空",
                "example": "nums = [3, 1, 4, 1, 5, 9]\nnums.append(2)       # [3,1,4,1,5,9,2]\nnums.sort()          # [1,1,2,3,4,5,9]\nnums.pop()           # 删除9\nprint(nums.index(3)) # 3的位置是3\nprint(nums.count(1)) # 1出现了2次",
                "exercise": {
                    "description": "输入 n 和 n 个整数，存入列表后输出：\n第一行：排序后的列表（空格隔开）\n第二行：最大值和最小值",
                    "template": "",
                    "sample_input": "5\n3 7 1 9 4",
                    "sample_output": "1 3 4 7 9\n9 1"
                }
            },
            {
                "concept": "列表切片：lst[start:end:step]\n  start - 起始下标（包含）\n  end   - 结束下标（不包含）\n  step  - 步长\n\n省略规则：\n  lst[:3]   → 前3个\n  lst[2:]   → 从第2个到最后\n  lst[::2]  → 每隔一个取一个\n  lst[::-1] → 反转列表\n\n切片不会报越界错误！",
                "example": "nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\nprint(nums[2:5])     # [2, 3, 4]\nprint(nums[:4])      # [0, 1, 2, 3]\nprint(nums[5:])      # [5, 6, 7, 8, 9]\nprint(nums[::2])     # [0, 2, 4, 6, 8]\nprint(nums[::-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]",
                "exercise": {
                    "description": "输入 10 个整数存入列表，输出：\n1. 第3到第7个元素（下标2到6）\n2. 所有偶数下标的元素\n3. 反转后的列表\n\n输入：0 1 2 3 4 5 6 7 8 9",
                    "template": "",
                    "sample_input": "0 1 2 3 4 5 6 7 8 9",
                    "sample_output": "2 3 4 5 6\n0 2 4 6 8\n9 8 7 6 5 4 3 2 1 0"
                }
            }
        ]
    },
    {
        "id": 9,
        "name": "字符串深入 - 文本处理",
        "phase": "第2阶段：控制流程",
        "steps": [
            {
                "concept": "字符串是不可变的序列，支持索引、切片，用法和列表类似。\n\n字符串常用方法：\n  s.upper()      - 转大写\n  s.lower()      - 转小写\n  s.strip()      - 去首尾空格\n  s.split()      - 按空格分割成列表\n  s.split(',')   - 按逗号分割\n  s.join(lst)    - 用s连接列表\n  s.replace(a,b) - 替换\n  s.find(x)      - 查找，返回位置（找不到返回-1）\n  s.count(x)     - 统计出现次数",
                "example": "s = \"  Hello, Python World!  \"\nprint(s.strip())           # \"Hello, Python World!\"\nprint(s.upper())           # \"  HELLO, PYTHON WORLD!  \"\nprint(s.split())           # ['Hello,', 'Python', 'World!']\n\nwords = [\"apple\", \"banana\", \"cherry\"]\nprint(\", \".join(words))   # \"apple, banana, cherry\"\n\nprint(s.find(\"Python\"))   # 9\nprint(s.replace(\"World\", \"编程\"))",
                "exercise": {
                    "description": "输入一句英文，统计其中有多少个单词（单词之间用空格隔开）。\n\n输入：I love Python programming\n输出：4",
                    "template": "",
                    "sample_input": "I love Python programming",
                    "sample_output": "4"
                }
            },
            {
                "concept": "字符串的 is 系列判断方法：\n  s.isdigit()  - 是否全是数字\n  s.isalpha()  - 是否全是字母\n  s.isalnum()  - 是否字母或数字\n  s.isupper()  - 是否全大写\n  s.islower()  - 是否全小写\n  s.isspace()  - 是否全是空格\n  s.startswith(x) - 是否以x开头\n  s.endswith(x)   - 是否以x结尾",
                "example": "s = \"Hello123\"\nprint(s.isalnum())   # True\nprint(s.isalpha())   # False（有数字）\nprint(s.isdigit())   # False（有字母）\nprint(s.startswith(\"He\"))  # True\nprint(s.endswith(\"23\"))    # True\n\n# 统计字符类型\ntext = \"Hello 123 World\"\nletters = sum(1 for c in text if c.isalpha())\ndigits = sum(1 for c in text if c.isdigit())\nprint(f\"字母：{letters}，数字：{digits}\")",
                "exercise": {
                    "description": "输入一行字符串，统计其中大写字母、小写字母和数字的个数。\n输出格式：大写个数 小写个数 数字个数\n\n输入：Hello123World\n输出：2 8 3",
                    "template": "",
                    "sample_input": "Hello123World",
                    "sample_output": "2 8 3"
                }
            },
            {
                "concept": "字符串反转：s[::-1]\n判断回文：s == s[::-1]\n\n字符串的 in 操作符：判断子串是否在字符串中。\n  \"Py\" in \"Python\"  → True\n\nin 也适用于列表、元组等序列。",
                "example": "s = \"上海自来水来自海上\"\nif s == s[::-1]:\n    print(\"是回文！\")\n\n# 检查敏感词\ncontent = \"Python是最好的编程语言\"\nif \"编程\" in content:\n    print(\"包含敏感词\")",
                "exercise": {
                    "description": "输入一个字符串，判断它是否是对称的（正着读和反着读一样）。\n是输出\"Yes\"，否则输出\"No\"。\n\n例如：\"abcba\" → Yes\n      \"abcde\" → No",
                    "template": "",
                    "sample_input": "abcba",
                    "sample_output": "Yes"
                }
            }
        ]
    },

    # ============================================================
    # 第3阶段：数据结构进阶 (10-14课)
    # ============================================================
    {
        "id": 10,
        "name": "元组与集合",
        "phase": "第3阶段：数据结构进阶",
        "steps": [
            {
                "concept": "元组（tuple）用圆括号 ()，和列表类似但不可修改（只读）。\n\n  point = (3, 4)     # 创建元组\n  single = (1,)       # 单元素元组要加逗号\n  x, y = point        # 解包\n\n元组的优点：\n• 比列表快\n• 可以作为字典的键\n• 数据安全（不可修改）",
                "example": "# 创建与访问\npoint = (3, 4)\nprint(point[0], point[1])  # 3 4\n\n# 解包（特别方便！）\na, b = point\n\n# 函数返回多个值（实际上返回的是元组）\ndef divmod(a, b):\n    return a // b, a % b\n\nq, r = divmod(17, 5)\nprint(q, r)  # 3 2",
                "exercise": {
                    "description": "输入两个点的坐标 (x1,y1) 和 (x2,y2)，计算两点之间的距离。\n公式：distance = sqrt((x2-x1)² + (y2-y1)²)\n结果保留2位小数。\n\n提示：import math; math.sqrt(x)\n\n输入：0 0 3 4\n输出：5.00",
                    "template": "import math\n\nx1, y1, x2, y2 = map(float, input().split())\n",
                    "sample_input": "0 0 3 4",
                    "sample_output": "5.00"
                }
            },
            {
                "concept": "集合（set）用花括号 {}，数学上的集合概念。\n特点：无序、不重复。\n\n常用操作：\n  s = {1, 2, 3}\n  s.add(x)      - 添加\n  s.remove(x)   - 删除\n  x in s        - 判断是否在集合中\n  len(s)        - 大小\n\n集合运算：\n  &  交集  |  并集  -  差集  ^ 对称差",
                "example": "s1 = {1, 2, 3, 4, 5}\ns2 = {4, 5, 6, 7, 8}\n\nprint(s1 & s2)  # {4, 5} 交集\nprint(s1 | s2)  # {1,2,3,4,5,6,7,8} 并集\nprint(s1 - s2)  # {1, 2, 3} 差集\n\n# 去重\nnums = [1, 2, 2, 3, 3, 3, 4]\nunique = list(set(nums))\nprint(unique)  # [1, 2, 3, 4]",
                "exercise": {
                    "description": "输入两行，每行若干个整数（空格隔开），输出它们的交集。\n\n输入：\n1 2 3 4 5\n4 5 6 7 8\n输出：4 5",
                    "template": "a = set(map(int, input().split()))\nb = set(map(int, input().split()))\n",
                    "sample_input": "1 2 3 4 5\n4 5 6 7 8",
                    "sample_output": "4 5"
                }
            }
        ]
    },
    {
        "id": 11,
        "name": "字典 - 键值对存储",
        "phase": "第3阶段：数据结构进阶",
        "steps": [
            {
                "concept": "字典（dict）用花括号 {} 存储键值对。\n\n  student = {\"name\": \"小明\", \"age\": 18}\n  print(student[\"name\"])  # 通过键访问\n  student[\"score\"] = 95   # 添加新键值对\n\n特点：\n• 键必须是不可变类型（字符串、数字、元组）\n• 值可以是任意类型\n• Python 3.7+ 保持插入顺序",
                "example": "student = {\n    \"name\": \"小明\",\n    \"age\": 18,\n    \"score\": 95.5\n}\n\nprint(student[\"name\"])    # 小明\nprint(student.get(\"grade\", \"无\"))  # 安全访问，没有返回默认值\n\n# 修改\nstudent[\"score\"] = 98\n\n# 添加新键\nstudent[\"city\"] = \"北京\"\nprint(student)",
                "exercise": {
                    "description": "创建一个字典保存一本书的信息：\n  book = {\"title\": \"Python编程\", \"author\": \"张三\", \"price\": 59.9}\n输出 book[\"title\"] 和 book[\"price\"]。\n\n输出格式：两行，第一行书名，第二行价格",
                    "template": "book = {\"title\": \"Python编程\", \"author\": \"张三\", \"price\": 59.9}\n",
                    "sample_input": "",
                    "sample_output": "Python编程\n59.9"
                }
            },
            {
                "concept": "字典的遍历和常用方法：\n  d.keys()      - 所有键\n  d.values()    - 所有值\n  d.items()     - 所有键值对\n  d.get(k, 默认值) - 安全获取\n  d.pop(k)      - 删除并返回值\n  d.update(d2)  - 合并另一个字典\n\n遍历：for k, v in d.items():",
                "example": "scores = {\"张三\": 85, \"李四\": 92, \"王五\": 78}\n\n# 遍历键值对\nfor name, score in scores.items():\n    print(f\"{name}: {score}分\")\n\n# 只遍历键\nfor name in scores:\n    print(name, end=\" \")\nprint()\n\n# 获取所有成绩\nall_scores = list(scores.values())\nprint(f\"平均分：{sum(all_scores)/len(all_scores):.1f}\")",
                "exercise": {
                    "description": "输入 3 个学生的姓名和成绩，存入字典，输出所有学生信息和平均分。\n\n输入格式：三行，每行 姓名 成绩\n输出：每行 \"姓名:成绩\"，最后一行 \"平均分:xx.x\"\n\n输入：\n张三 85\n李四 92\n王五 78\n输出：\n张三:85\n李四:92\n王五:78\n平均分:85.0",
                    "template": "scores = {}\nfor _ in range(3):\n    name, score = input().split()\n    \n\n",
                    "sample_input": "张三 85\n李四 92\n王五 78",
                    "sample_output": "张三:85\n李四:92\n王五:78\n平均分:85.0"
                }
            }
        ]
    },
    {
        "id": 12,
        "name": "列表推导式与高级循环技巧",
        "phase": "第3阶段：数据结构进阶",
        "steps": [
            {
                "concept": "列表推导式（List Comprehension）是Python最优雅的特性之一。\n\n基本语法：[表达式 for 变量 in 序列]\n  [x*x for x in range(5)]  → [0, 1, 4, 9, 16]\n\n带条件：[表达式 for 变量 in 序列 if 条件]\n  [x for x in range(10) if x%2==0]  → [0, 2, 4, 6, 8]\n\n也可以用于字典和集合推导式。",
                "example": "# 列表推导式\nsquares = [x**2 for x in range(1, 11)]\nprint(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]\n\n# 带条件\nevens = [x for x in range(20) if x % 2 == 0]\nprint(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]\n\n# 双层循环\npairs = [(i, j) for i in range(3) for j in range(3)]\nprint(pairs)  # [(0,0), (0,1), (0,2), (1,0), (1,1), ...]",
                "exercise": {
                    "description": "用列表推导式，生成 1 到 50 中所有能被 3 整除的数。\n输出这些数，空格隔开。",
                    "template": "nums = [x for x in range(1, 51) if x % 3 == 0]\n",
                    "sample_input": "",
                    "sample_output": "3 6 9 12 15 18 21 24 27 30 33 36 39 42 45 48"
                }
            },
            {
                "concept": "enumerate() 同时获取下标和值：\n  for i, v in enumerate(lst):\n\nzip() 并行遍历多个序列：\n  for a, b in zip(list1, list2):\n\nsorted() 排序：\n  sorted(lst)         # 升序\n  sorted(lst, reverse=True)  # 降序\n  sorted(lst, key=len)  # 按长度排序",
                "example": "names = [\"张三\", \"李四\", \"王五\"]\nscores = [85, 92, 78]\n\n# enumerate 获取下标\nfor i, name in enumerate(names):\n    print(f\"第{i+1}名：{name}\")\n\n# zip 并行遍历\nfor name, score in zip(names, scores):\n    print(f\"{name}: {score}\")\n\n# sorted 排序\nprint(sorted(scores))                     # [78, 85, 92]\nprint(sorted(names, key=len))             # 按名字长度排序",
                "exercise": {
                    "description": "输入 3 名学生的姓名和成绩，按成绩从高到低排序后输出。\n每行格式：\"姓名 成绩\"\n\n输入：\n张三 85\n李四 92\n王五 78\n输出：\n李四 92\n张三 85\n王五 78",
                    "template": "students = []\nfor _ in range(3):\n    name, score = input().split()\n    \n\n",
                    "sample_input": "张三 85\n李四 92\n王五 78",
                    "sample_output": "李四 92\n张三 85\n王五 78"
                }
            }
        ]
    },
    {
        "id": 13,
        "name": "函数 - 组织代码的艺术",
        "phase": "第4阶段：函数与模块",
        "steps": [
            {
                "concept": "函数用 def 定义，把一段代码打包复用：\n\n  def 函数名(参数):\n      代码\n      return 返回值\n\n特点：\n• 不需要写返回值类型\n• 没有参数也可以不写参数\n• 没有 return 返回 None\n• 可以先调用再定义...不行！必须定义在前",
                "example": "def add(a, b):\n    \"\"\"返回两个数的和\"\"\"  # 文档字符串\n    return a + b\n\nresult = add(3, 5)\nprint(result)  # 8\n\n# 文档字符串可以用 help() 查看\nhelp(add)",
                "exercise": {
                    "description": "编写函数 is_even(n)，判断整数是否为偶数。\n在 main 中读入一个数，调用函数后输出\"Yes\"或\"No\"。",
                    "template": "def is_even(n):\n    \n\nn = int(input())\n",
                    "sample_input": "6",
                    "sample_output": "Yes"
                }
            },
            {
                "concept": "参数的高级用法：\n1. 默认参数：def f(a, b=10):  （b默认为10）\n2. 关键字参数：f(b=5, a=3)  （按名传参）\n3. 可变参数：*args 接收任意数量位置参数\n4. 关键字可变参数：**kwargs 接收任意数量关键字参数",
                "example": "# 默认参数\ndef greet(name, greeting=\"你好\"):\n    print(f\"{greeting}，{name}！\")\n\ngreet(\"小明\")          # 你好，小明！\ngreet(\"Tom\", \"Hello\") # Hello，Tom！\n\n# 可变参数\ndef sum_all(*nums):\n    return sum(nums)\n\nprint(sum_all(1, 2, 3, 4, 5))  # 15\n\n# **kwargs\ndef show_info(**info):\n    for k, v in info.items():\n        print(f\"{k}: {v}\")\n\nshow_info(name=\"小明\", age=18, city=\"北京\")",
                "exercise": {
                    "description": "编写函数 calc(a, b, op)，实现一个简易计算器：\nop 为 \"+\" \"-\" \"*\" \"/\" 时分别做加减乘除。\nop 为其他值时返回 \"无效运算符\"。\n\n输入：3 + 5\n输出：8\n\n注意：输入用空格隔开三个部分",
                    "template": "def calc(a, b, op):\n    \n\n# 注意：输入的第二部分是运算符字符串\n",
                    "sample_input": "3 + 5",
                    "sample_output": "8"
                }
            },
            {
                "concept": "变量作用域：\n• 函数内定义的变量是局部变量\n• 函数外定义的变量是全局变量\n• 函数内可以访问全局变量，但修改要用 global\n• 尽量少用全局变量！\n\nPython 的 LEGB 规则：\nLocal → Enclosing → Global → Built-in",
                "example": "x = 10  # 全局变量\n\ndef func():\n    y = 20  # 局部变量\n    print(x)  # 可以访问全局变量\n    \n    # 要修改全局变量必须用 global\n    global x\n    x = 100\n\nfunc()\nprint(x)  # 100",
                "exercise": {
                    "description": "编写函数，输入一个数 n，返回它的斐波那契数列第 n 项。\nF(1)=1, F(2)=1, F(n)=F(n-1)+F(n-2)\n\n输入：6\n输出：8 （因为数列：1,1,2,3,5,8）",
                    "template": "def fib(n):\n    \n\nn = int(input())\n",
                    "sample_input": "6",
                    "sample_output": "8"
                }
            }
        ]
    },
    {
        "id": 14,
        "name": "lambda与高阶函数",
        "phase": "第4阶段：函数与模块",
        "steps": [
            {
                "concept": "lambda 表达式（匿名函数）：\n  lambda 参数: 表达式\n\n相当于：\n  def f(参数): return 表达式\n\n常用于需要简单函数的场合，如排序的 key、filter、map 等。",
                "example": "# 普通函数 vs lambda\n\ndef double(x):\n    return x * 2\n\ndouble_lambda = lambda x: x * 2\n\nprint(double(5))       # 10\nprint(double_lambda(5)) # 10\n\n# 排序时指定 key\nstudents = [(\"张三\", 85), (\"李四\", 92), (\"王五\", 78)]\nstudents.sort(key=lambda s: s[1])\nprint(students)  # [(\"王五\",78), (\"张三\",85), (\"李四\",92)]",
                "exercise": {
                    "description": "输入 3 个整数，用 lambda 表达式作为 key，按数字的绝对值从大到小排序后输出。\n\n输入：-5 3 -8 1\n输出：-8 -5 3 1",
                    "template": "",
                    "sample_input": "-5 3 -8 1",
                    "sample_output": "-8 -5 3 1"
                }
            },
            {
                "concept": "map()、filter() 和 reduce() 是三个重要的高阶函数：\n\n  map(函数, 序列)    - 对每个元素应用函数\n  filter(函数, 序列)  - 过滤出满足条件的元素\n  reduce(函数, 序列)  - 累积计算\n\nPython 3 中 map/filter 返回迭代器，可用 list() 转为列表。\n更推荐用列表推导式！",
                "example": "nums = [1, 2, 3, 4, 5]\n\n# map：每个数平方\nsquared = list(map(lambda x: x**2, nums))\nprint(squared)  # [1, 4, 9, 16, 25]\n\n# filter：选出偶数\nevens = list(filter(lambda x: x % 2 == 0, nums))\nprint(evens)  # [2, 4]\n\n# 列表推导式更简洁！\nprint([x**2 for x in nums])       # [1, 4, 9, 16, 25]\nprint([x for x in nums if x%2==0])  # [2, 4]",
                "exercise": {
                    "description": "输入一行整数，用 map 和 filter 完成：\n1. 用 map 将每个数转为它的平方\n2. 用 filter 选出平方后大于 50 的数\n3. 输出结果列表，空格隔开\n\n输入：3 5 7 9 11\n输出：81 121",
                    "template": "",
                    "sample_input": "3 5 7 9 11",
                    "sample_output": "81 121"
                }
            }
        ]
    },
    {
        "id": 15,
        "name": "递归 - 函数调用自己",
        "phase": "第4阶段：函数与模块",
        "steps": [
            {
                "concept": "递归：函数调用自身。\n\n两个要素：\n1. 终止条件（base case）—— 不再递归的条件\n2. 递归步骤 —— 把问题缩小\n\n经典例子：阶乘\n  n! = n * (n-1)!\n  0! = 1",
                "example": "def factorial(n):\n    if n <= 1:  # 终止条件\n        return 1\n    return n * factorial(n - 1)  # 递归\n\nprint(factorial(5))  # 120\n\n# 执行过程：\n# factorial(5)\n# = 5 * factorial(4)\n# = 5 * 4 * factorial(3)\n# = 5 * 4 * 3 * factorial(2)\n# = 5 * 4 * 3 * 2 * factorial(1)\n# = 5 * 4 * 3 * 2 * 1 = 120",
                "exercise": {
                    "description": "用递归实现 n 的阶乘。\n输入 n（1 <= n <= 10），输出 n!。",
                    "template": "def factorial(n):\n    \n\nn = int(input())\n",
                    "sample_input": "5",
                    "sample_output": "120"
                }
            },
            {
                "concept": "递归的优缺点：\n优点：代码简洁，符合数学定义\n缺点：\n• 效率低（大量重复计算）\n• 有深度限制（默认1000层）\n\n优化方案：记忆化递归（缓存中间结果）\n\n斐波那契数列：F(n) = F(n-1) + F(n-2)",
                "example": "# 普通递归（效率低）\ndef fib(n):\n    if n <= 2:\n        return 1\n    return fib(n-1) + fib(n-2)\n\n# 带缓存的递归（高效）\nfrom functools import lru_cache\n\n@lru_cache(maxsize=None)\ndef fib_fast(n):\n    if n <= 2:\n        return 1\n    return fib_fast(n-1) + fib_fast(n-2)\n\nprint(fib_fast(50))  # 12586269025，瞬间出结果",
                "exercise": {
                    "description": "用递归计算斐波那契数列第 n 项。\nF(1)=1, F(2)=1\n\n输入：10\n输出：55",
                    "template": "def fib(n):\n    if n <= 2:\n        return 1\n    \n\nn = int(input())\n",
                    "sample_input": "10",
                    "sample_output": "55"
                }
            }
        ]
    },
    {
        "id": 16,
        "name": "模块与包 - 使用标准库",
        "phase": "第4阶段：函数与模块",
        "steps": [
            {
                "concept": "Python 最大的优势之一就是丰富的标准库。\n\n导入方式：\n  import math              # 导入整个模块\n  from math import sqrt     # 导入特定函数\n  import math as m          # 起别名\n  from math import *        # 导入所有（不推荐）\n\n常用标准库：\n  math    - 数学函数\n  random  - 随机数\n  datetime - 日期时间\n  os      - 操作系统\n  json    - JSON处理\n  re      - 正则表达式",
                "example": "import math\n\nprint(math.pi)           # 3.141592653589793\nprint(math.sqrt(16))     # 4.0\nprint(math.sin(math.radians(30)))  # 0.5\nprint(math.floor(3.7))   # 3\nprint(math.ceil(3.2))    # 4\n\n# 常用的数学常数\nprint(math.e)            # 2.718281828459045\nprint(math.inf)          # 无穷大\nprint(math.nan)          # 非数字",
                "exercise": {
                    "description": "用 math 模块计算：\n输入半径 r，输出圆的面积（π取 math.pi）和平方根（面积开方）。\n结果保留2位小数。\n\n输入：10\n输出：314.16\n17.72",
                    "template": "import math\n\nr = float(input())\n",
                    "sample_input": "10",
                    "sample_output": "314.16\n17.72"
                }
            },
            {
                "concept": "random 模块 - 生成随机数：\n  random.random()     - [0,1)随机小数\n  random.randint(a,b) - [a,b]随机整数\n  random.choice(lst)  - 随机选一个\n  random.shuffle(lst) - 打乱列表\n  random.sample(lst, k) - 随机选k个不重复\n\ndatetime 模块 - 日期时间：\n  datetime.now()      - 当前时间\n  date.today()        - 今天日期\n  timedelta(days=1)   - 时间差",
                "example": "import random\n\n# 随机整数\nprint(random.randint(1, 100))  # 1-100随机\n\n# 随机选一个\nfruits = [\"苹果\", \"香蕉\", \"橘子\", \"草莓\"]\nprint(random.choice(fruits))\n\n# 打乱\nrandom.shuffle(fruits)\nprint(fruits)\n\n# 随机密码\nimport string\npassword = ''.join(random.choices(string.ascii_letters + string.digits, k=8))\nprint(f\"随机密码：{password}\")",
                "exercise": {
                    "description": "用 random 模块模拟掷骰子：\n输入掷的次数 n，输出每次掷骰子的结果（1-6），空格隔开。\n\n输入：5\n输出示例：3 5 2 6 1（随机结果，每次不同）",
                    "template": "import random\n\nn = int(input())\n",
                    "sample_input": "5",
                    "sample_output": "3 5 2 6 1"
                }
            }
        ]
    },
    {
        "id": 17,
        "name": "文件操作 - 数据的持久化",
        "phase": "第4阶段：函数与模块",
        "steps": [
            {
                "concept": "文件操作三步：打开 → 读写 → 关闭\n\n推荐用 with 语句（自动关闭）：\n  with open(\"文件\", \"模式\", encoding=\"utf-8\") as f:\n      f.read() / f.write()\n\n常用模式：\n  \"r\"    读取（默认）\n  \"w\"    写入（覆盖）\n  \"a\"    追加\n  \"r+\"   读写\n  \"rb\"   二进制读\n  \"wb\"   二进制写",
                "example": "# 写入文件\nwith open(\"test.txt\", \"w\", encoding=\"utf-8\") as f:\n    f.write(\"第一行\\n\")\n    f.write(\"第二行\\n\")\nprint(\"写入完成\")\n\n# 读取所有内容\nwith open(\"test.txt\", \"r\", encoding=\"utf-8\") as f:\n    content = f.read()\nprint(content)\n\n# 逐行读取\nwith open(\"test.txt\", \"r\", encoding=\"utf-8\") as f:\n    for line in f:\n        print(line.strip())",
                "exercise": {
                    "description": "输入一个字符串和文件名，将该字符串写入文件，再读取出来输出。\n输出格式：\"写入成功：[文件名]，内容：[字符串]\"\n\n输入：\nHello World\ndata.txt\n输出：\n写入成功：data.txt，内容：Hello World",
                    "template": "content = input()\nfilename = input()\n",
                    "sample_input": "Hello World\ndata.txt",
                    "sample_output": "写入成功：data.txt，内容：Hello World"
                }
            },
            {
                "concept": "json 模块 - 读写JSON数据（Python与文件之间的桥梁）：\n\n  import json\n  json.dump(数据, 文件)  - 写入JSON\n  json.load(文件)       - 读取JSON\n  json.dumps(数据)      - 转为JSON字符串\n  json.loads(字符串)    - 从JSON字符串解析\n\nJSON支持的数据类型：\n字符串、数字、布尔、列表、字典、None",
                "example": "import json\n\n# 写入JSON\ndata = {\n    \"name\": \"小明\",\n    \"age\": 18,\n    \"scores\": [85, 92, 78],\n    \"is_pass\": True\n}\n\nwith open(\"data.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n\n# 读取JSON\nwith open(\"data.json\", \"r\", encoding=\"utf-8\") as f:\n    loaded = json.load(f)\n\nprint(loaded[\"name\"])  # 小明\nprint(loaded[\"scores\"])  # [85, 92, 78]",
                "exercise": {
                    "description": "创建一个字典表示一本书：\n  book = {\"title\": \"Python实战\", \"price\": 49.9}\n用 json.dumps 转为字符串后输出。\n\n输出格式：JSON字符串",
                    "template": "import json\n\nbook = {\"title\": \"Python实战\", \"price\": 49.9}\n",
                    "sample_input": "",
                    "sample_output": "{\"title\": \"Python实战\", \"price\": 49.9}"
                }
            }
        ]
    },
    {
        "id": 18,
        "name": "异常处理 - 优雅地处理错误",
        "phase": "第5阶段：面向对象与异常",
        "steps": [
            {
                "concept": "异常处理让程序在出错时不崩溃，而是做出合适的反应。\n\n  try:\n      可能出错的代码\n  except 错误类型 as e:\n      处理方式\n\n常见异常：\n  ValueError    - 值错误\n  ZeroDivisionError - 除零错误\n  FileNotFoundError - 文件未找到\n  TypeError    - 类型错误\n  IndexError   - 索引越界\n  KeyError     - 键不存在",
                "example": "try:\n    x = int(input(\"请输入整数：\"))\n    result = 10 / x\n    print(f\"10/{x} = {result}\")\nexcept ValueError:\n    print(\"输入的不是整数！\")\nexcept ZeroDivisionError:\n    print(\"不能除0！\")\nexcept Exception as e:\n    print(f\"其他错误：{e}\")\nelse:\n    print(\"计算成功！\")\nfinally:\n    print(\"程序结束。\")",
                "exercise": {
                    "description": "输入两个整数 a 和 b，输出 a/b 的结果。\n如果 b=0，输出\"除数不能为0\"，而不是让程序崩溃。\n如果输入的不是整数，输出\"输入错误\"。",
                    "template": "try:\n    a = int(input())\n    b = int(input())\n    \nexcept ZeroDivisionError:\n    \nexcept ValueError:\n    \n",
                    "sample_input": "10\n0",
                    "sample_output": "除数不能为0"
                }
            },
            {
                "concept": "自定义异常和主动抛出：\n  raise 异常类型(\"描述信息\")\n\n可以用 class 定义自己的异常类：\n  class MyError(Exception):\n      pass",
                "example": "def withdraw(balance, amount):\n    if amount > balance:\n        raise ValueError(f\"余额不足！只有{balance}元\")\n    return balance - amount\n\ntry:\n    new_balance = withdraw(100, 150)\nexcept ValueError as e:\n    print(f\"取款失败：{e}\")\n\n# 自定义异常类\nclass AgeError(Exception):\n    pass\n\ndef set_age(age):\n    if age < 0 or age > 150:\n        raise AgeError(f\"年龄不合法：{age}\")\n    print(f\"年龄设为：{age}\")",
                "exercise": {
                    "description": "编写函数 my_sqrt(x)，如果 x < 0 就 raise ValueError(\"负数不能开平方\")。\n否则返回平方根。\n\n在 main 中测试：输入一个数，调用 my_sqrt，捕获异常并输出错误信息。\n\n输入：-9\n输出：错误：负数不能开平方",
                    "template": "import math\n\ndef my_sqrt(x):\n    if x < 0:\n        raise ValueError(\"负数不能开平方\")\n    return math.sqrt(x)\n\ntry:\n    n = float(input())\n    \nexcept ValueError as e:\n    \n",
                    "sample_input": "-9",
                    "sample_output": "错误：负数不能开平方"
                }
            }
        ]
    },
    {
        "id": 19,
        "name": "面向对象 - 类与对象",
        "phase": "第5阶段：面向对象与异常",
        "steps": [
            {
                "concept": "面向对象编程（OOP）把数据和操作打包成对象。\n\n  class 类名:\n      def __init__(self, 参数):\n          self.属性 = 值\n      \n      def 方法(self):\n          ...\n\n__init__ 是构造函数，创建对象时自动调用。\nself 代表当前对象（相当于其他语言的 this）。\n所有方法的第一个参数必须是 self。",
                "example": "class Student:\n    def __init__(self, name, age, score):\n        self.name = name\n        self.age = age\n        self.score = score\n    \n    def say_hello(self):\n        print(f\"大家好，我是{self.name}，今年{self.age}岁\")\n    \n    def is_pass(self):\n        return self.score >= 60\n\n# 创建对象\nstu = Student(\"小明\", 18, 85)\nstu.say_hello()\nprint(f\"是否及格：{stu.is_pass()}\")",
                "exercise": {
                    "description": "定义 Rectangle 类：\n- __init__(self, width, height) 初始化\n- area() 方法返回面积\n\n输入宽和高，输出面积。\n\n输入：4 6\n输出：24",
                    "template": "class Rectangle:\n    def __init__(self, width, height):\n        self.width = width\n        self.height = height\n    \n    \n\nw, h = map(int, input().split())\nrect = Rectangle(w, h)\nprint(rect.area())",
                    "sample_input": "4 6",
                    "sample_output": "24"
                }
            },
            {
                "concept": "封装：用 _ 或 __ 表示私有属性。\n  _name   → 约定为私有（实际上可以访问）\n  __name  → 名称修饰，外部不能直接访问\n\n@property 装饰器：把方法变成属性访问。\n  @property       → getter\n  @属性名.setter  → setter",
                "example": "class BankAccount:\n    def __init__(self, owner, balance):\n        self.owner = owner\n        self.__balance = balance  # 私有属性\n    \n    def deposit(self, amount):\n        if amount > 0:\n            self.__balance += amount\n    \n    @property\n    def balance(self):  # 像属性一样访问\n        return self.__balance\n    \n    @balance.setter\n    def balance(self, amount):\n        if amount >= 0:\n            self.__balance = amount\n\nacc = BankAccount(\"小明\", 1000)\nprint(acc.balance)  # 1000\nacc.deposit(500)\nprint(acc.balance)  # 1500",
                "exercise": {
                    "description": "定义一个 Circle 类：\n- 私有属性：__radius\n- @property 获取半径\n- @radius.setter 设置半径（必须>0）\n- area() 方法计算面积\n\n输入半径，输出面积（保留2位小数）。",
                    "template": "import math\n\nclass Circle:\n    def __init__(self, r):\n        self.__radius = r\n    \n    @property\n    def radius(self):\n        return self.__radius\n    \n    \n    \n    def area(self):\n        \n\nr = float(input())\nc = Circle(r)\n",
                    "sample_input": "5",
                    "sample_output": "78.54"
                }
            }
        ]
    },
    {
        "id": 20,
        "name": "继承 - 代码复用",
        "phase": "第5阶段：面向对象与异常",
        "steps": [
            {
                "concept": "继承让子类获得父类的属性和方法，实现代码复用。\n\n  class 子类(父类):\n      def __init__(self, ...):\n          super().__init__(...)  # 调用父类构造\n\n特点：\n• 子类可以重写父类方法\n• 子类可以添加新方法\n• 支持多层继承\n• 支持多继承（但慎用）",
                "example": "class Animal:\n    def __init__(self, name):\n        self.name = name\n    \n    def speak(self):\n        print(f\"{self.name}发出声音\")\n\nclass Dog(Animal):\n    def __init__(self, name, breed):\n        super().__init__(name)  # 调用父类构造\n        self.breed = breed\n    \n    def speak(self):  # 重写父类方法\n        print(f\"{self.name}（{self.breed}）汪汪叫！\")\n\nclass Cat(Animal):\n    def speak(self):\n        print(f\"{self.name}喵喵叫～\")\n\ndog = Dog(\"旺财\", \"金毛\")\ncat = Cat(\"咪咪\")\ndog.speak()\ncat.speak()",
                "exercise": {
                    "description": "定义基类 Shape：\n- __init__(self, name)\n- area() 返回 0\n\n定义子类 Square：\n- __init__(self, side)\n- area() 返回 side*side\n\n输入边长，输出面积。",
                    "template": "class Shape:\n    def __init__(self, name):\n        self.name = name\n    def area(self):\n        return 0\n\nclass Square(Shape):\n    \n\nside = float(input())\nsq = Square(side)\n",
                    "sample_input": "4",
                    "sample_output": "16"
                }
            }
        ]
    },
    {
        "id": 21,
        "name": "魔术方法 - 让对象更Pythonic",
        "phase": "第5阶段：面向对象与异常",
        "steps": [
            {
                "concept": "魔术方法（Magic Methods）是Python类的特殊方法，用双下划线包围。\n\n常用魔术方法：\n  __str__   → print(obj)时调用\n  __repr__  → 调试时显示\n  __len__   → len(obj)时调用\n  __add__   → obj1 + obj2\n  __eq__    → obj1 == obj2\n  __lt__    → obj1 < obj2\n  __getitem__ → obj[key]",
                "example": "class Vector:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n    \n    def __str__(self):\n        return f\"({self.x}, {self.y})\"\n    \n    def __add__(self, other):\n        return Vector(self.x + other.x, self.y + other.y)\n    \n    def __eq__(self, other):\n        return self.x == other.x and self.y == other.y\n    \n    def __abs__(self):\n        return (self.x**2 + self.y**2) ** 0.5\n\nv1 = Vector(3, 4)\nv2 = Vector(1, 2)\nprint(v1)           # (3, 4)\nprint(v1 + v2)      # (4, 6)\nprint(v1 == Vector(3, 4))  # True\nprint(abs(v1))      # 5.0",
                "exercise": {
                    "description": "为 Rectangle 类添加 __str__ 方法，使其输出 \"矩形(宽x高)\"。\n\n输入宽和高，创建对象，print 输出。\n\n输入：4 6\n输出：矩形(4x6)",
                    "template": "class Rectangle:\n    def __init__(self, w, h):\n        self.w = w\n        self.h = h\n    \n    \n\nw, h = map(int, input().split())\nr = Rectangle(w, h)\nprint(r)",
                    "sample_input": "4 6",
                    "sample_output": "矩形(4x6)"
                }
            }
        ]
    },
    {
        "id": 22,
        "name": "综合实战 - 学生成绩管理系统",
        "phase": "第6阶段：综合实战",
        "steps": [
            {
                "concept": "现在用学过的所有知识做一个完整的学生成绩管理系统！\n\n功能需求：\n1. 添加学生（姓名、学号、成绩）\n2. 显示所有学生\n3. 计算平均分\n4. 按成绩排序\n5. 查找学生\n6. 保存到文件\n\n面向对象设计：\n- Student 类：表示一个学生\n- StudentManager 类：管理所有学生",
                "example": "class Student:\n    def __init__(self, name, sid, score):\n        self.name = name\n        self.sid = sid\n        self.score = score\n    \n    def __str__(self):\n        return f\"{self.name} {self.sid} {self.score}\"\n\nclass StudentManager:\n    def __init__(self):\n        self.students = []\n    \n    def add(self, name, sid, score):\n        self.students.append(Student(name, sid, score))\n    \n    def show_all(self):\n        for s in self.students:\n            print(s)\n    \n    def avg_score(self):\n        if not self.students:\n            return 0\n        return sum(s.score for s in self.students) / len(self.students)",
                "exercise": {
                    "description": "实现完整的 Student 类，支持：\n1. 输入 n 个学生\n2. 输出所有学生信息\n3. 输出平均分（保留1位小数）\n\n输入：\n3\n张三 1001 85.5\n李四 1002 92.0\n王五 1003 78.5\n输出：\n张三 1001 85.5\n李四 1002 92.0\n王五 1003 78.5\n平均分：85.3",
                    "template": "class Student:\n    def __init__(self, name, sid, score):\n        self.name = name\n        self.sid = sid\n        self.score = score\n    \n    def display(self):\n        \n\nn = int(input())\nstudents = []\nfor _ in range(n):\n    name, sid, score = input().split()\n    \n\nprint(f\"平均分：{avg:.1f}\")",
                    "sample_input": "3\n张三 1001 85.5\n李四 1002 92.0\n王五 1003 78.5",
                    "sample_output": "张三 1001 85.5\n李四 1002 92.0\n王五 1003 78.5\n平均分：85.3"
                }
            },
            {
                "concept": "增强版学生管理系统：增加排序和查找功能。\n\n排序：sorted(students, key=lambda s: s.score, reverse=True)\n查找：filter(lambda s: s.name == name, students)\n\n可以使用 json 模块保存到文件。",
                "example": "# 按成绩排序\nsorted_stu = sorted(manager.students, \n                    key=lambda s: s.score, \n                    reverse=True)\nfor s in sorted_stu:\n    print(s)\n\n# 查找学生\ndef find_by_name(self, name):\n    results = [s for s in self.students if name in s.name]\n    return results\n\n# 保存到文件\nimport json\ndef save(self, filename):\n    data = [{\"name\": s.name, \"sid\": s.sid, \"score\": s.score} \n            for s in self.students]\n    with open(filename, \"w\") as f:\n        json.dump(data, f, ensure_ascii=False, indent=2)",
                "exercise": {
                    "description": "在上一个练习的基础上，增加按成绩从高到低排序后输出。\n\n输入：\n3\n张三 1001 85.5\n李四 1002 92.0\n王五 1003 78.5\n输出：\n李四 1002 92.0\n张三 1001 85.5\n王五 1003 78.5",
                    "template": "class Student:\n    def __init__(self, name, sid, score):\n        self.name = name\n        self.sid = sid\n        self.score = float(score)\n    \n    def display(self):\n        print(f\"{self.name} {self.sid} {self.score}\")\n\nn = int(input())\nstudents = []\nfor _ in range(n):\n    name, sid, score = input().split()\n    \n\n",
                    "sample_input": "3\n张三 1001 85.5\n李四 1002 92.0\n王五 1003 78.5",
                    "sample_output": "李四 1002 92.0\n张三 1001 85.5\n王五 1003 78.5"
                }
            }
        ]
    },
    {
        "id": 23,
        "name": "装饰器与生成器",
        "phase": "第6阶段：综合实战",
        "steps": [
            {
                "concept": "装饰器（Decorator）是修改函数功能的语法糖：\n\n  @decorator\n  def func():\n      ...\n\n等价于 func = decorator(func)\n\n装饰器常用于：日志记录、性能测试、权限验证、缓存等。",
                "example": "import time\n\n# 计时装饰器\ndef timer(func):\n    def wrapper(*args, **kwargs):\n        start = time.time()\n        result = func(*args, **kwargs)\n        end = time.time()\n        print(f\"{func.__name__} 耗时：{end-start:.4f}秒\")\n        return result\n    return wrapper\n\n@timer\ndef slow_function():\n    total = sum(range(1000000))\n    return total\n\nresult = slow_function()\nprint(result)",
                "exercise": {
                    "description": "编写一个重复执行 n 次的装饰器 @repeat(n)。\n\n@repeat(3)\ndef say_hello():\n    print(\"Hello!\")\n\nsay_hello()  # 会输出3次 Hello!\n\n请在下方实现并测试。",
                    "template": "def repeat(n):\n    def decorator(func):\n        def wrapper(*args, **kwargs):\n            for _ in range(n):\n                func(*args, **kwargs)\n        return wrapper\n    return decorator\n\n@repeat(3)\ndef say_hello():\n    print(\"Hello!\")\n\nsay_hello()",
                    "sample_input": "",
                    "sample_output": "Hello!\nHello!\nHello!"
                }
            },
            {
                "concept": "生成器（Generator）用 yield 关键字，可以生成大量数据而不占用内存。\n\n  def count_up_to(n):\n      i = 1\n      while i <= n:\n          yield i\n          i += 1\n\n和列表的区别：\n• 列表一次性生成所有元素\n• 生成器用的时候才生成，节省内存\n\n生成器表达式：(x for x in range(100))",
                "example": "# 生成器：斐波那契数列\ndef fibonacci(n):\n    a, b = 0, 1\n    count = 0\n    while count < n:\n        yield a\n        a, b = b, a + b\n        count += 1\n\n# 用 for 遍历生成器\nfor num in fibonacci(10):\n    print(num, end=\" \")  # 0 1 1 2 3 5 8 13 21 34\nprint()\n\n# 生成器表达式\nsquares = (x**2 for x in range(10))\nprint(sum(squares))  # 285\n\n# 比较内存占用\nimport sys\nlist_comp = [x for x in range(10000)]\ngen_expr = (x for x in range(10000))\nprint(sys.getsizeof(list_comp))  # 约 85176\nprint(sys.getsizeof(gen_expr))   # 约 104（非常小！）",
                "exercise": {
                    "description": "用生成器实现一个函数 even_numbers(n)，生成前 n 个偶数。\n\n输入 n，输出前 n 个偶数，空格隔开。\n\n输入：6\n输出：0 2 4 6 8 10",
                    "template": "def even_numbers(n):\n    \n\nn = int(input())\n",
                    "sample_input": "6",
                    "sample_output": "0 2 4 6 8 10"
                }
            }
        ]
    },
    {
        "id": 24,
        "name": "综合挑战 - 通讯录管理系统",
        "phase": "第6阶段：综合实战",
        "steps": [
            {
                "concept": "最终项目：设计并实现一个通讯录管理系统。\n\n需求：\n1. 添加联系人（姓名、电话、邮箱）\n2. 显示所有联系人\n3. 按姓名查找\n4. 删除联系人\n5. 保存到JSON文件\n\n使用知识：\n• 类与对象\n• 列表与字典\n• 文件操作\n• 异常处理\n• 排序\n• 字符串处理",
                "example": "class Contact:\n    def __init__(self, name, phone, email=\"\"):\n        self.name = name\n        self.phone = phone\n        self.email = email\n    \n    def __str__(self):\n        return f\"{self.name} | {self.phone} | {self.email}\"\n\nclass AddressBook:\n    def __init__(self):\n        self.contacts = []\n    \n    def add(self, name, phone, email=\"\"):\n        self.contacts.append(Contact(name, phone, email))\n    \n    def search(self, keyword):\n        return [c for c in self.contacts \n                if keyword.lower() in c.name.lower()]\n    \n    def delete(self, name):\n        self.contacts = [c for c in self.contacts \n                        if c.name != name]\n    \n    def sort_by_name(self):\n        self.contacts.sort(key=lambda c: c.name)",
                "exercise": {
                    "description": "实现 AddressBook 通讯录系统的基本功能：\n1. 添加 n 个联系人（姓名、电话）\n2. 输出所有联系人\n\n输入：\n2\n张三 13800138000\n李四 13900139000\n输出：\n张三 | 13800138000\n李四 | 13900139000",
                    "template": "class Contact:\n    def __init__(self, name, phone):\n        self.name = name\n        self.phone = phone\n    \n    def __str__(self):\n        return f\"{self.name} | {self.phone}\"\n\nn = int(input())\ncontacts = []\nfor _ in range(n):\n    name, phone = input().split()\n    \n\n",
                    "sample_input": "2\n张三 13800138000\n李四 13900139000",
                    "sample_output": "张三 | 13800138000\n李四 | 13900139000"
                }
            },
            {
                "concept": "通讯录增强版：实现按姓名查找和排序功能。\n\n查找：用列表推导式过滤\n  results = [c for c in contacts if keyword in c.name]\n\n排序：用 sorted() 或 list.sort()\n  sorted(contacts, key=lambda c: c.name)",
                "example": "# 查找联系人\ndef search(self, keyword):\n    found = [c for c in self.contacts \n             if keyword.lower() in c.name.lower()]\n    return found\n\n# 使用示例\nbook = AddressBook()\nbook.add(\"张三\", \"13800138000\")\nbook.add(\"张四\", \"13700137000\")\nbook.add(\"李四\", \"13900139000\")\n\nresults = book.search(\"张\")\nfor c in results:\n    print(c)\n# 张三 | 13800138000\n# 张四 | 13700137000\n\nprint(\"---\")\nbook.sort_by_name()\nfor c in book.contacts:\n    print(c)",
                "exercise": {
                    "description": "实现按姓名查找功能：\n1. 输入 n 个联系人\n2. 输入要查找的关键词\n3. 输出所有姓名中包含该关键词的联系人\n\n输入：\n3\n张三 13800138000\n张伟 13700137000\n李四 13900139000\n张\n输出：\n张三 | 13800138000\n张伟 | 13700137000",
                    "template": "class Contact:\n    def __init__(self, name, phone):\n        self.name = name\n        self.phone = phone\n    def __str__(self):\n        return f\"{self.name} | {self.phone}\"\n\nn = int(input())\ncontacts = []\nfor _ in range(n):\n    name, phone = input().split()\n    contacts.append(Contact(name, phone))\n\nkeyword = input()\n",
                    "sample_input": "3\n张三 13800138000\n张伟 13700137000\n李四 13900139000\n张",
                    "sample_output": "张三 | 13800138000\n张伟 | 13700137000"
                }
            }
        ]
    }
]

PHASES_PYTHON = [
    "第1阶段：Python基础入门",
    "第2阶段：控制流程",
    "第3阶段：数据结构进阶",
    "第4阶段：函数与模块",
    "第5阶段：面向对象与异常",
    "第6阶段：综合实战"
]
