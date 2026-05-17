# -*- coding: utf-8 -*-

lessons_cpp = [

    # ============================================================
    # 第1阶段：C++基础入门 (0-4课)
    # ============================================================
    {
        "id": 0,
        "name": "第一个C++程序 - Hello World",
        "phase": "第1阶段：C++基础入门",
        "steps": [
            {
                "concept": "每个C++程序都必须有一个 main 函数，程序从这里开始执行。\n\n基本框架：\n  #include <iostream>    // 引入输入输出库\n  using namespace std;    // 使用标准命名空间\n  \n  int main() {           // 主函数\n      cout << ...;        // 输出\n      return 0;           // 返回0表示成功\n  }\n\n注意：每条语句末尾必须有分号 ;",
                "example": "#include <iostream>\nusing namespace std;\n\nint main() {\n    cout << \"Hello, World!\" << endl;\n    return 0;\n}",
                "exercise": {
                    "description": "编写程序，输出你的名字（可以输出任意名字）",
                    "template": "#include <iostream>\nusing namespace std;\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "",
                    "sample_output": "小明"
                }
            },
            {
                "concept": "endl 表示换行（end line）。\n转义字符：\n  \\n  换行\n  \\t  制表符\n  \\\" 双引号\n  \\\\ 反斜杠\n\n多个 cout 会输出在同一行，除非加了 endl 或 \\n。",
                "example": "cout << \"第一行\" << endl;\ncout << \"第二行\";\ncout << \"还在第二行\" << endl;\ncout << \"制表符:\\t缩进\" << endl;",
                "exercise": {
                    "description": "分两行输出：\n第一行：I love C++\n第二行：Hello World",
                    "template": "#include <iostream>\nusing namespace std;\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "",
                    "sample_output": "I love C++\nHello World"
                }
            }
        ]
    },
    {
        "id": 1,
        "name": "变量与数据类型",
        "phase": "第1阶段：C++基础入门",
        "steps": [
            {
                "concept": "C++是静态类型语言，变量必须先声明类型再使用：\n\n  数据类型 变量名 = 值;\n\n基本数据类型：\n  int     整数 (4字节)        例：int age = 18;\n  double  双精度小数 (8字节)   例：double pi = 3.14;\n  float   单精度小数 (4字节)   例：float f = 3.14f;\n  char    单个字符 (1字节)    例：char c = 'A';\n  bool    布尔值 (1字节)     例：bool ok = true;\n\n变量名规则：字母/数字/下划线，不能数字开头，不能是关键字。",
                "example": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int age = 18;\n    double price = 99.5;\n    char grade = 'A';\n    bool isPass = true;\n    \n    cout << \"年龄：\" << age << endl;\n    cout << \"价格：\" << price << endl;\n    cout << \"等级：\" << grade << endl;\n    cout << \"是否通过：\" << isPass << endl;  // true输出为1\n    return 0;\n}",
                "exercise": {
                    "description": "声明一个 int 变量 score，赋值为100，然后输出它。",
                    "template": "#include <iostream>\nusing namespace std;\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "",
                    "sample_output": "100"
                }
            },
            {
                "concept": "字符串类型需要包含 <string> 头文件：\n  #include <string>\n  string name = \"小明\";\n\ncout 可以输出多个内容，用 << 连接：\n  cout << \"姓名：\" << name << \"，年龄：\" << age << endl;\n\nsizeof 运算符可以查看类型占用的字节数：\n  cout << sizeof(int);  // 4",
                "example": "#include <iostream>\n#include <string>\nusing namespace std;\n\nint main() {\n    string name = \"小明\";\n    int age = 18;\n    \n    cout << \"我叫\" << name << \"，今年\" << age << \"岁\" << endl;\n    \n    cout << \"int占用\" << sizeof(int) << \"字节\" << endl;\n    cout << \"double占用\" << sizeof(double) << \"字节\" << endl;\n    return 0;\n}",
                "exercise": {
                    "description": "声明两个变量：\n  string name = \"张三\";\n  int age = 20;\n输出：\"我叫张三，今年20岁\"\n\n提示：需要 #include <string>",
                    "template": "#include <iostream>\n#include <string>\nusing namespace std;\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "",
                    "sample_output": "我叫张三，今年20岁"
                }
            },
            {
                "concept": "类型转换：\n  隐式转换：int → double 自动转\n  显式转换（强制类型转换）：\n    double x = 3.14;\n    int a = (int)x;       // C风格\n    int b = int(x);        // 函数风格\n    int c = static_cast<int>(x);  // C++风格（推荐）",
                "example": "double pi = 3.14159;\nint a = (int)pi;              // 3\nint b = static_cast<int>(pi); // 3（推荐）\n\ndouble result = 5 / 2;            // 2.0（整数除法！）\ndouble result2 = 5 / 2.0;         // 2.5\ndouble result3 = (double)5 / 2;   // 2.5\n\ncout << a << \" \" << result << \" \" << result2 << endl;",
                "exercise": {
                    "description": "输入两个整数 a 和 b，输出 a/b 的精确小数结果。\n提示：用 (double)a / b\n\n输入：5 2\n输出：2.5",
                    "template": "#include <iostream>\nusing namespace std;\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "5 2",
                    "sample_output": "2.5"
                }
            }
        ]
    },
    {
        "id": 2,
        "name": "输入输出与格式化",
        "phase": "第1阶段：C++基础入门",
        "steps": [
            {
                "concept": "cin >> 用于从键盘读入数据：\n  int age;\n  cin >> age;\n\n可以一次读多个：\n  cin >> a >> b >> c;\n\n输入时会自动跳过空格和换行。\n\n注意：cin >> 遇到空格会停止读取，读字符串时要注意。",
                "example": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int a, b;\n    cout << \"请输入两个整数：\";\n    cin >> a >> b;\n    cout << \"和 = \" << a + b << endl;\n    return 0;\n}",
                "exercise": {
                    "description": "输入两个整数 a 和 b，输出它们的和与差。\n第一行和，第二行差。\n\n输入：10 3\n输出：13\n7",
                    "template": "#include <iostream>\nusing namespace std;\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "10 3",
                    "sample_output": "13\n7"
                }
            },
            {
                "concept": "格式化输出——设置小数位数：\n  #include <iomanip>\n  cout << fixed;           // 固定小数模式\n  cout << setprecision(2); // 保留2位小数\n  cout << setw(5);         // 设置宽度\n  cout << setfill('0');    // 填充字符",
                "example": "#include <iostream>\n#include <iomanip>\nusing namespace std;\n\nint main() {\n    double pi = 3.1415926535;\n    \n    cout << fixed << setprecision(2);\n    cout << \"保留2位：\" << pi << endl;\n    \n    cout << fixed << setprecision(4);\n    cout << \"保留4位：\" << pi << endl;\n    \n    // 设置宽度\n    cout << setw(8) << setfill('0') << 42 << endl;\n    return 0;\n}",
                "exercise": {
                    "description": "输入圆的半径 r，输出周长和面积。\n周长 = 2 * 3.14 * r\n面积 = 3.14 * r * r\n结果保留2位小数。\n\n输入：5\n输出：31.40\n78.50",
                    "template": "#include <iostream>\n#include <iomanip>\nusing namespace std;\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "5",
                    "sample_output": "31.40\n78.50"
                }
            },
            {
                "concept": "getline() 读取含空格的整行：\n  string line;\n  getline(cin, line);  // 读取整行\n\n注意：getline 之前如果有 cin >>，需要用 cin.ignore() 吃掉换行符。",
                "example": "#include <iostream>\n#include <string>\nusing namespace std;\n\nint main() {\n    string name;\n    cout << \"请输入全名：\";\n    getline(cin, name);  // 可以读取 \"张三 李四\"\n    cout << \"你好，\" << name << endl;\n    return 0;\n}",
                "exercise": {
                    "description": "输入一行字符串（可能包含空格），然后输出它。\n\n输入：Hello C++ World\n输出：Hello C++ World\n\n提示：用 getline(cin, s)",
                    "template": "#include <iostream>\n#include <string>\nusing namespace std;\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "Hello C++ World",
                    "sample_output": "Hello C++ World"
                }
            }
        ]
    },
    {
        "id": 3,
        "name": "算术运算符与表达式",
        "phase": "第1阶段：C++基础入门",
        "steps": [
            {
                "concept": "算术运算符：\n  +  加法     -  减法\n  *  乘法     /  除法（整数相除取整！）\n  %  取模（求余数）\n\n重点：整数除法会舍弃小数部分！\n  5 / 2 = 2  （不是2.5！）\n  5 % 2 = 1  （5除以2余1）\n  -5 % 2 = -1（余数符号和被除数一致）",
                "example": "int a = 10, b = 3;\ncout << a << \" + \" << b << \" = \" << a + b << endl;  // 13\ncout << a << \" - \" << b << \" = \" << a - b << endl;  // 7\ncout << a << \" * \" << b << \" = \" << a * b << endl;  // 30\ncout << a << \" / \" << b << \" = \" << a / b << endl;  // 3（整数除法！）\ncout << a << \" % \" << b << \" = \" << a % b << endl;  // 1",
                "exercise": {
                    "description": "输入两个整数 a 和 b，输出它们的和、差、积、商（整除）、余数。\n每行一个结果。\n\n输入：17 5\n输出：22\n12\n85\n3\n2",
                    "template": "#include <iostream>\nusing namespace std;\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "17 5",
                    "sample_output": "22\n12\n85\n3\n2"
                }
            },
            {
                "concept": "复合赋值运算符：\n  +=    a += 1  等价于 a = a + 1\n  -=    a -= 1\n  *=    a *= 2\n  /=    a /= 2\n  %=    a %= 2\n\n自增自减：\n  i++   先取值再加1（后置）\n  ++i   先加1再取值（前置）\n  i--   先取值再减1\n  --i   先减1再取值",
                "example": "int x = 10;\nx += 5;    // x = 15\nx *= 2;    // x = 30\ncout << x << endl;\n\n// 前置和后置的区别\nint a = 5, b = 5;\ncout << a++ << endl;  // 输出5，然后a变为6\ncout << ++b << endl;  // b先变为6，然后输出6\ncout << a << \" \" << b << endl;  // 6 6",
                "exercise": {
                    "description": "输入 n，输出 n 的平方和立方。\n\n输入：5\n输出：25\n125\n\n提示：不用乘方函数，直接用 n*n 和 n*n*n",
                    "template": "#include <iostream>\nusing namespace std;\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "5",
                    "sample_output": "25\n125"
                }
            }
        ]
    },
    {
        "id": 4,
        "name": "条件判断 - if/else/switch",
        "phase": "第1阶段：C++基础入门",
        "steps": [
            {
                "concept": "if 语句：\n  if (条件) {\n      // 条件为真时执行\n  } else {\n      // 条件为假时执行\n  }\n\n比较运算符：== != > < >= <=\n逻辑运算符：&&（与） ||（或） !（非）\n\n注意：C++ 用 == 判断相等，= 是赋值！",
                "example": "int score;\ncin >> score;\n\nif (score >= 60) {\n    cout << \"及格了！\" << endl;\n} else {\n    cout << \"不及格...\" << endl;\n}\n\n// 逻辑运算符\nint age;\ncin >> age;\nif (age >= 18 && age <= 60) {\n    cout << \"成年人\" << endl;\n}",
                "exercise": {
                    "description": "输入一个整数，判断奇偶数。\n偶数输出\"偶数\"，奇数输出\"奇数\"。\n\n提示：x % 2 == 0 是偶数",
                    "template": "#include <iostream>\nusing namespace std;\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "7",
                    "sample_output": "奇数"
                }
            },
            {
                "concept": "多分支：if ... else if ... else\n  if (条件1) {\n      ...\n  } else if (条件2) {\n      ...\n  } else if (条件3) {\n      ...\n  } else {\n      ...\n  }\n\nswitch 语句（处理整数/字符的多分支）：\n  switch (变量) {\n      case 值1: ... break;\n      case 值2: ... break;\n      default: ... break;\n  }",
                "example": "// if-else if 多分支\nint score;\ncin >> score;\nif (score >= 90) {\n    cout << \"优秀\" << endl;\n} else if (score >= 80) {\n    cout << \"良好\" << endl;\n} else if (score >= 60) {\n    cout << \"及格\" << endl;\n} else {\n    cout << \"不及格\" << endl;\n}\n\n// switch 示例\nint month;\ncin >> month;\nswitch (month) {\n    case 3: case 4: case 5:\n        cout << \"春季\" << endl; break;\n    case 6: case 7: case 8:\n        cout << \"夏季\" << endl; break;\n    case 9: case 10: case 11:\n        cout << \"秋季\" << endl; break;\n    case 12: case 1: case 2:\n        cout << \"冬季\" << endl; break;\n    default:\n        cout << \"无效月份\" << endl;\n}",
                "exercise": {
                    "description": "输入月份（1-12），输出季节：\n3-5月 → Spring\n6-8月 → Summer\n9-11月 → Autumn\n12-2月 → Winter\n\n输入：4\n输出：Spring",
                    "template": "#include <iostream>\nusing namespace std;\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "4",
                    "sample_output": "Spring"
                }
            },
            {
                "concept": "三目运算符：条件 ? 值1 : 值2\n  int max = (a > b) ? a : b;  // 取较大值\n\n嵌套 if：if 里再套 if。\n注意 else 会匹配最近的 if。用花括号避免歧义。",
                "example": "// 三目运算符\nint a = 10, b = 20;\nint max_val = (a > b) ? a : b;\ncout << \"较大值：\" << max_val << endl;\n\n// 嵌套 if\nint year;\ncin >> year;\nif (year % 4 == 0) {\n    if (year % 100 == 0) {\n        if (year % 400 == 0)\n            cout << \"闰年\" << endl;\n        else\n            cout << \"平年\" << endl;\n    } else\n        cout << \"闰年\" << endl;\n} else\n    cout << \"平年\" << endl;",
                "exercise": {
                    "description": "输入三个整数，用三目运算符找出最大值并输出。\n\n输入：3 7 5\n输出：7\n\n提示：int m = (a>b) ? a : b; m = (m>c) ? m : c;",
                    "template": "#include <iostream>\nusing namespace std;\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "3 7 5",
                    "sample_output": "7"
                }
            }
        ]
    },

    # ============================================================
    # 第2阶段：控制流程 (5-8课)
    # ============================================================
    {
        "id": 5,
        "name": "for循环",
        "phase": "第2阶段：控制流程",
        "steps": [
            {
                "concept": "for 循环：知道循环次数时使用。\n\n  for (初始化; 条件; 更新) {\n      循环体\n  }\n\n执行顺序：初始化→条件判断→循环体→更新→再判断...\n\n常见写法：\n  for (int i = 0; i < n; i++)   // 0到n-1\n  for (int i = 1; i <= n; i++)  // 1到n\n  for (int i = n; i >= 0; i--)  // n到0",
                "example": "// 输出1到5\nfor (int i = 1; i <= 5; i++) {\n    cout << i << \" \";\n}\ncout << endl;\n\n// 倒序\nfor (int i = 5; i >= 1; i--) {\n    cout << i << \" \";\n}\ncout << endl;\n\n// 步长为2\nfor (int i = 0; i <= 10; i += 2) {\n    cout << i << \" \";\n}\ncout << endl;",
                "exercise": {
                    "description": "输入 n，输出 1 到 n 的所有整数，空格隔开。\n\n输入：5\n输出：1 2 3 4 5",
                    "template": "#include <iostream>\nusing namespace std;\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "5",
                    "sample_output": "1 2 3 4 5"
                }
            },
            {
                "concept": "累加求和模式：\n  int sum = 0;\n  for (int i = 1; i <= n; i++) {\n      sum += i;\n  }\n\n累乘求阶乘模式：\n  int fact = 1;\n  for (int i = 1; i <= n; i++) {\n      fact *= i;\n  }\n\n变量作用域：在 for 里定义的 i 只能在循环内使用。",
                "example": "// 1到n求和\nint n = 100;\nint sum = 0;\nfor (int i = 1; i <= n; i++) {\n    sum += i;\n}\ncout << \"1+\" << n << \"=\" << sum << endl;  // 5050\n\n// n! 阶乘\nint fact = 1;\nfor (int i = 1; i <= 5; i++) {\n    fact *= i;\n}\ncout << \"5! = \" << fact << endl;  // 120",
                "exercise": {
                    "description": "输入 n，计算 1 到 n 的和。\n\n输入：100\n输出：5050",
                    "template": "#include <iostream>\nusing namespace std;\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "100",
                    "sample_output": "5050"
                }
            },
            {
                "concept": "嵌套循环：循环里面套循环。\n外层每执行一次，内层执行一整遍。\n\n常用于打印图案、处理二维数据。\n\n注意循环变量的命名习惯：外层用 i，内层用 j。",
                "example": "// 打印直角三角形\nint n = 5;\nfor (int i = 1; i <= n; i++) {\n    for (int j = 1; j <= i; j++) {\n        cout << \"*\";\n    }\n    cout << endl;\n}\n// 输出：\n// *\n// **\n// ***\n// ****\n// *****\n\n// 九九乘法表\nfor (int i = 1; i <= 9; i++) {\n    for (int j = 1; j <= i; j++) {\n        cout << j << \"*\" << i << \"=\" << i*j << \"\\t\";\n    }\n    cout << endl;\n}",
                "exercise": {
                    "description": "输入 n，打印 n 行直角三角形星号图案。\nn=3 时输出：\n*\n**\n***",
                    "template": "#include <iostream>\nusing namespace std;\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "3",
                    "sample_output": "*\n**\n***"
                }
            }
        ]
    },
    {
        "id": 6,
        "name": "while循环与循环控制",
        "phase": "第2阶段：控制流程",
        "steps": [
            {
                "concept": "while 循环：不知道具体次数，只知道条件时用。\n  while (条件) {\n      循环体\n  }\n\ndo-while 循环：至少执行一次。\n  do {\n      循环体\n  } while (条件);  // 注意分号！",
                "example": "// 求各位数字之和\nint n = 1234;\nint sum = 0;\nwhile (n > 0) {\n    sum += n % 10;  // 取个位\n    n /= 10;         // 去掉个位\n}\ncout << sum << endl;  // 10\n\n// do-while 至少执行一次\nint x = 1;\ndo {\n    cout << x << \" \";\n    x++;\n} while (x <= 5);\ncout << endl;",
                "exercise": {
                    "description": "输入一个正整数，用 while 求各位数字之和。\n\n输入：1234\n输出：10\n\n提示：每次 n%10 取个位，n/10 去掉个位",
                    "template": "#include <iostream>\nusing namespace std;\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "1234",
                    "sample_output": "10"
                }
            },
            {
                "concept": "break - 立即退出整个循环。\ncontinue - 跳过本次循环剩余部分，进入下一次。\n\nwhile(true) 无限循环 + break 是常用模式。\n\n应用：\n• 判断素数（找到因数就break）\n• 输入验证（直到合法为止）\n• 搜索（找到就break）",
                "example": "// 判断素数\nint n = 17;\nbool isPrime = true;\nfor (int i = 2; i < n; i++) {\n    if (n % i == 0) {\n        isPrime = false;\n        break;  // 找到因数，退出循环\n    }\n}\ncout << (isPrime ? \"Yes\" : \"No\") << endl;\n\n// continue：跳过3的倍数\nfor (int i = 1; i <= 10; i++) {\n    if (i % 3 == 0) continue;\n    cout << i << \" \";  // 1 2 4 5 7 8 10\n}",
                "exercise": {
                    "description": "判断素数：输入 n（n>=2），是输出\"Yes\"，否则输出\"No\"。\n\n输入：17\n输出：Yes\n\n提示：从2循环到n-1检查能否整除",
                    "template": "#include <iostream>\nusing namespace std;\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "17",
                    "sample_output": "Yes"
                }
            }
        ]
    },
    {
        "id": 7,
        "name": "数组 - 存储多个数据",
        "phase": "第2阶段：控制流程",
        "steps": [
            {
                "concept": "数组声明：类型 数组名[大小];\n  int scores[5];        // 未初始化\n  int nums[5] = {1,2,3,4,5};  // 初始化\n  int arr[] = {1,2,3};   // 自动推大小\n\n访问元素：下标从0开始\n  nums[0] = 100;  // 修改第一个\n  cout << nums[2];  // 访问第三个\n\n遍历数组：for (int i = 0; i < 5; i++)",
                "example": "int nums[5] = {10, 20, 30, 40, 50};\n\n// 遍历\nfor (int i = 0; i < 5; i++) {\n    cout << nums[i] << \" \";\n}\ncout << endl;\n\n// 求和\nint sum = 0;\nfor (int i = 0; i < 5; i++) {\n    sum += nums[i];\n}\ncout << \"和 = \" << sum << endl;\ncout << \"平均 = \" << sum / 5.0 << endl;",
                "exercise": {
                    "description": "输入 n 和 n 个整数，存入数组后输出它们的和。\n\n输入：\n5\n1 2 3 4 5\n输出：15",
                    "template": "#include <iostream>\nusing namespace std;\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "5\n1 2 3 4 5",
                    "sample_output": "15"
                }
            },
            {
                "concept": "找最大值算法：\n  1. 假设第一个最大：int maxVal = arr[0];\n  2. 遍历剩下的：if (arr[i] > maxVal) maxVal = arr[i];\n\n二维数组：int matrix[3][4] = {{...}, {...}, {...}};\n  双重循环遍历。\n\n数组作为函数参数时会退化为指针。",
                "example": "// 找最大值和最小值\nint nums[] = {3, 8, 1, 9, 4, 2};\nint n = 6;\nint maxVal = nums[0], minVal = nums[0];\n\nfor (int i = 0; i < n; i++) {\n    if (nums[i] > maxVal) maxVal = nums[i];\n    if (nums[i] < minVal) minVal = nums[i];\n}\ncout << \"最大值：\" << maxVal << endl;\ncout << \"最小值：\" << minVal << endl;\n\n// 二维数组\nint matrix[2][3] = {{1,2,3}, {4,5,6}};\nfor (int i = 0; i < 2; i++) {\n    for (int j = 0; j < 3; j++) {\n        cout << matrix[i][j] << \" \";\n    }\n    cout << endl;\n}",
                "exercise": {
                    "description": "输入 n 和 n 个数，输出最大值和最小值。\n第一行最大值，第二行最小值。\n\n输入：\n6\n3 8 1 9 4 2\n输出：\n9\n1",
                    "template": "#include <iostream>\nusing namespace std;\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "6\n3 8 1 9 4 2",
                    "sample_output": "9\n1"
                }
            }
        ]
    },
    {
        "id": 8,
        "name": "字符串处理",
        "phase": "第2阶段：控制流程",
        "steps": [
            {
                "concept": "C++ 有两种字符串：\n1. C风格字符串（字符数组）：char str[] = \"Hello\";\n2. string 类（推荐）：#include <string>\n\nstring 常用操作：\n  s.length()  长度\n  s[i]        访问字符\n  s1 + s2     拼接\n  s.find(t)   查找\n  s.substr(pos, len)  子串\n  getline(cin, s)  读取一行",
                "example": "#include <iostream>\n#include <string>\nusing namespace std;\n\nint main() {\n    string s1 = \"Hello\";\n    string s2 = \" World\";\n    \n    string s3 = s1 + s2;\n    cout << s3 << endl;          // Hello World\n    cout << \"长度：\" << s3.length() << endl;\n    \n    // 遍历\n    for (int i = 0; i < s3.length(); i++) {\n        cout << s3[i] << \" \";\n    }\n    cout << endl;\n    \n    // 查找\n    int pos = s3.find(\"World\");\n    cout << \"World的位置：\" << pos << endl;\n    \n    // 子串\n    cout << s3.substr(0, 5) << endl;  // Hello\n    return 0;\n}",
                "exercise": {
                    "description": "输入一个字符串，输出它的反转结果。\n\n输入：hello\n输出：olleh\n\n提示：从后往前遍历输出",
                    "template": "#include <iostream>\n#include <string>\nusing namespace std;\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "hello",
                    "sample_output": "olleh"
                }
            },
            {
                "concept": "C风格字符串（C++兼容C的字符串方式）：\n  char s[] = \"Hello\";\n  char s[10] = {'H','e','l','l','o','\\0'};\n\n常用函数（需要 #include <cstring>）：\n  strlen(s)    长度\n  strcpy(d,s)  复制\n  strcat(d,s)  拼接\n  strcmp(a,b)  比较（相等返回0）",
                "example": "#include <iostream>\n#include <cstring>\nusing namespace std;\n\nint main() {\n    char s1[] = \"Hello\";\n    char s2[20];\n    \n    strcpy(s2, s1);        // 复制\n    strcat(s2, \" World\");  // 拼接\n    cout << s2 << endl;    // Hello World\n    \n    cout << \"长度：\" << strlen(s2) << endl;\n    \n    // 比较\n    if (strcmp(s1, \"Hello\") == 0) {\n        cout << \"相等\" << endl;\n    }\n    return 0;\n}",
                "exercise": {
                    "description": "统计字符：输入一行字符串（不含空格），统计其中大写字母和小写字母的个数。\n\n判断大写：c >= 'A' && c <= 'Z'\n判断小写：c >= 'a' && c <= 'z'\n\n输出格式：大写个数 小写个数\n\n输入：HelloWorld\n输出：2 8",
                    "template": "#include <iostream>\n#include <string>\nusing namespace std;\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "HelloWorld",
                    "sample_output": "2 8"
                }
            }
        ]
    },

    # ============================================================
    # 第3阶段：函数与指针 (9-13课)
    # ============================================================
    {
        "id": 9,
        "name": "函数 - 代码模块化",
        "phase": "第3阶段：函数与指针",
        "steps": [
            {
                "concept": "函数定义：\n  返回值类型 函数名(参数列表) {\n      函数体\n      return 返回值;\n  }\n\nvoid 表示无返回值。\n函数必须先定义后使用，或者先声明后定义。",
                "example": "#include <iostream>\nusing namespace std;\n\n// 函数定义\nint add(int a, int b) {\n    return a + b;\n}\n\n// void函数\nvoid sayHello(string name) {\n    cout << \"你好，\" << name << \"！\" << endl;\n}\n\nint main() {\n    cout << add(3, 5) << endl;  // 8\n    sayHello(\"小明\");\n    return 0;\n}",
                "exercise": {
                    "description": "编写函数 bool isEven(int n)，判断整数是否为偶数。\n在 main 中读入一个数，调用函数后输出\"Yes\"或\"No\"。",
                    "template": "#include <iostream>\nusing namespace std;\n\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "6",
                    "sample_output": "Yes"
                }
            },
            {
                "concept": "函数高级特性：\n1. 函数重载：同名不同参数\n2. 默认参数：void f(int a, int b = 10)\n3. 内联函数：inline 关键字（建议编译器内联）\n4. 引用参数：void swap(int &a, int &b) — 可以修改原变量",
                "example": "#include <iostream>\nusing namespace std;\n\n// 函数重载\nint max(int a, int b) {\n    return (a > b) ? a : b;\n}\ndouble max(double a, double b) {\n    return (a > b) ? a : b;\n}\n\n// 引用传参\nvoid swap(int &a, int &b) {\n    int temp = a;\n    a = b;\n    b = temp;\n}\n\nint main() {\n    cout << max(3, 5) << endl;     // 调用int版\n    cout << max(3.14, 2.5) << endl; // 调用double版\n    \n    int x = 10, y = 20;\n    swap(x, y);\n    cout << x << \" \" << y << endl;  // 20 10\n    return 0;\n}",
                "exercise": {
                    "description": "编写函数 double area(double r)，计算半径为r的圆的面积。\n公式：面积 = 3.14159 * r * r\n在main中读入r，调用函数输出面积（保留2位小数）。",
                    "template": "#include <iostream>\n#include <iomanip>\nusing namespace std;\n\n\nint main() {\n    double r;\n    cin >> r;\n    \n    return 0;\n}",
                    "sample_input": "3",
                    "sample_output": "28.27"
                }
            },
            {
                "concept": "递归：函数调用自身。\n\n两个要素：\n1. 终止条件（不再递归的情况）\n2. 递归公式（问题规模缩小）\n\n经典例子：\n  int fact(int n) {\n      if (n <= 1) return 1;\n      return n * fact(n-1);\n  }\n\n递归的执行过程：递推（向下）→ 回归（向上）",
                "example": "#include <iostream>\nusing namespace std;\n\n// 阶乘递归\nint factorial(int n) {\n    if (n <= 1) return 1;\n    return n * factorial(n - 1);\n}\n\n// 斐波那契数列递归\nint fib(int n) {\n    if (n <= 2) return 1;\n    return fib(n-1) + fib(n-2);\n}\n\nint main() {\n    cout << \"5! = \" << factorial(5) << endl;  // 120\n    cout << \"fib(10) = \" << fib(10) << endl;  // 55\n    return 0;\n}",
                "exercise": {
                    "description": "用递归实现n的阶乘。\n输入 n（1<=n<=10），输出 n!。",
                    "template": "#include <iostream>\nusing namespace std;\n\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "5",
                    "sample_output": "120"
                }
            }
        ]
    },
    {
        "id": 10,
        "name": "指针 - 内存地址",
        "phase": "第3阶段：函数与指针",
        "steps": [
            {
                "concept": "指针存储变量的内存地址。\n\n  int num = 42;\n  int* p = &num;  // p保存num的地址\n  \n  & 取地址运算符\n  * 解引用运算符（访问指针指向的值）\n\n类比：变量=房子，指针=写着地址的纸条。",
                "example": "int num = 42;\nint* p = &num;\n\ncout << \"num的值：\" << num << endl;      // 42\ncout << \"num的地址：\" << &num << endl;   // 0x...\ncout << \"指针p的值：\" << p << endl;      // 0x...\ncout << \"通过指针访问：\" << *p << endl; // 42\n\n// 通过指针修改值\n*p = 100;\ncout << \"修改后：\" << num << endl;      // 100\n\n// 指针的大小\ncout << \"指针大小：\" << sizeof(p) << \"字节\" << endl;",
                "exercise": {
                    "description": "编写程序，用指针交换两个变量的值。\n\nvoid swap(int* a, int* b) {\n    int temp = *a;\n    *a = *b;\n    *b = temp;\n}\n\n输入：5 8\n输出：8 5",
                    "template": "#include <iostream>\nusing namespace std;\n\n\nint main() {\n    int x, y;\n    cin >> x >> y;\n    \n    return 0;\n}",
                    "sample_input": "5 8",
                    "sample_output": "8 5"
                }
            },
            {
                "concept": "指针和数组：数组名就是首地址。\n  int arr[5] = {10, 20, 30, 40, 50};\n  int* p = arr;  // 等价于 &arr[0]\n  p[i] 等价于 arr[i] 等价于 *(p+i)\n\n指针运算：\n  p++ 移动到下一个元素（不是下一个字节！）\n  p + n 偏移n个元素\n\n空指针：int* p = nullptr;（C++11推荐）",
                "example": "int arr[5] = {10, 20, 30, 40, 50};\nint* p = arr;  // 指向数组第一个元素\n\n// 通过指针遍历\nfor (int i = 0; i < 5; i++) {\n    cout << *(p + i) << \" \";  // 等价于 p[i]\n}\ncout << endl;\n\n// 指针移动\ncout << *p << endl;     // 10\np++;\ncout << *p << endl;     // 20\np += 2;\ncout << *p << endl;     // 40\n\n// 动态内存分配\nint* q = new int(42);\ncout << *q << endl;  // 42\ndelete q;  // 释放内存",
                "exercise": {
                    "description": "用指针对数组求和。\n输入 n 和 n 个整数，用指针遍历数组并输出和。\n\n输入：\n5\n1 2 3 4 5\n输出：15",
                    "template": "#include <iostream>\nusing namespace std;\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "5\n1 2 3 4 5",
                    "sample_output": "15"
                }
            }
        ]
    },
    {
        "id": 11,
        "name": "引用与动态内存",
        "phase": "第3阶段：函数与指针",
        "steps": [
            {
                "concept": "引用（Reference）是变量的别名：\n  int num = 10;\n  int &ref = num;  // ref是num的引用\n  ref = 20;        // 相当于 num = 20\n\n引用和指针的区别：\n• 引用必须初始化，指针可以不\n• 引用不能改指向，指针可以\n• 引用更安全，语法更简洁\n\n引用主要用于函数参数（避免拷贝，可以修改原值）。",
                "example": "#include <iostream>\nusing namespace std;\n\n// 引用传参\nvoid increment(int &n) {\n    n++;  // 直接修改原变量\n}\n\nint main() {\n    int num = 10;\n    int &ref = num;\n    \n    cout << num << endl;  // 10\n    ref = 20;\n    cout << num << endl;  // 20\n    \n    increment(num);\n    cout << num << endl;  // 21\n    \n    return 0;\n}",
                "exercise": {
                    "description": "编写函数 void calculate(int a, int b, int &sum, int &product)，\n计算 a 和 b 的和与积，通过引用返回。\n\n输入：4 7\n输出：11 28",
                    "template": "#include <iostream>\nusing namespace std;\n\n\nint main() {\n    int x, y;\n    cin >> x >> y;\n    \n    return 0;\n}",
                    "sample_input": "4 7",
                    "sample_output": "11 28"
                }
            },
            {
                "concept": "动态内存分配：\n  int* p = new int;       // 分配一个整数\n  int* arr = new int[10]; // 分配数组\n  delete p;               // 释放单个\n  delete[] arr;           // 释放数组\n\n忘记 delete 会导致内存泄漏！\n现代C++推荐使用智能指针（#include <memory>）：\n  unique_ptr<int> p = make_unique<int>(42);",
                "example": "#include <iostream>\nusing namespace std;\n\nint main() {\n    // 动态分配\n    int* p = new int(42);\n    cout << *p << endl;  // 42\n    delete p;\n    \n    // 动态数组\n    int n = 5;\n    int* arr = new int[n];\n    for (int i = 0; i < n; i++) {\n        arr[i] = i * 10;\n    }\n    for (int i = 0; i < n; i++) {\n        cout << arr[i] << \" \";\n    }\n    delete[] arr;\n    \n    return 0;\n}",
                "exercise": {
                    "description": "用 new 动态分配一个整数，输入一个数存入，输出它，然后 delete 释放。\n\n输入：42\n输出：42",
                    "template": "#include <iostream>\nusing namespace std;\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "42",
                    "sample_output": "42"
                }
            }
        ]
    },

    # ============================================================
    # 第4阶段：面向对象 (12-16课)
    # ============================================================
    {
        "id": 12,
        "name": "类与对象",
        "phase": "第4阶段：面向对象编程",
        "steps": [
            {
                "concept": "类（class）是面向对象的核心。\n\n  class 类名 {\n  public:      // 公共成员\n      数据类型 属性;\n      void 方法() { }\n  };\n\n创建对象：\n  类名 对象名;\n  对象名.属性 = 值;\n  对象名.方法();",
                "example": "#include <iostream>\n#include <string>\nusing namespace std;\n\nclass Student {\npublic:\n    string name;\n    int age;\n    double score;\n    \n    void sayHello() {\n        cout << \"大家好，我是\" << name << endl;\n    }\n    \n    bool isPass() {\n        return score >= 60;\n    }\n};\n\nint main() {\n    Student stu;\n    stu.name = \"小明\";\n    stu.age = 18;\n    stu.score = 85.5;\n    \n    stu.sayHello();\n    cout << \"是否及格：\" << (stu.isPass() ? \"是\" : \"否\") << endl;\n    return 0;\n}",
                "exercise": {
                    "description": "定义 Rectangle 类：\n- 属性：int width, height\n- 方法：int area() 返回面积\n\n输入宽和高，输出面积。\n\n输入：4 6\n输出：24",
                    "template": "#include <iostream>\nusing namespace std;\n\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "4 6",
                    "sample_output": "24"
                }
            },
            {
                "concept": "构造函数：和类同名、无返回值，创建对象时自动调用。\n\n  class Book {\n  public:\n      string title;\n      // 无参构造\n      Book() { title = \"未命名\"; }\n      // 带参构造\n      Book(string t) { title = t; }\n  };\n\n初始化列表（推荐）：\n  Book(string t) : title(t) { }",
                "example": "#include <iostream>\n#include <string>\nusing namespace std;\n\nclass Book {\npublic:\n    string title;\n    string author;\n    int pages;\n    \n    // 无参构造\n    Book() : title(\"未命名\"), author(\"未知\"), pages(0) {}\n    \n    // 带参构造（初始化列表）\n    Book(string t, string a, int p) \n        : title(t), author(a), pages(p) {}\n    \n    void show() {\n        cout << \"《\" << title << \"》—— \" << author << \" (\" << pages << \"页)\" << endl;\n    }\n};\n\nint main() {\n    Book b1;  // 无参\n    Book b2(\"C++编程\", \"张三\", 500);  // 带参\n    b1.show();\n    b2.show();\n    return 0;\n}",
                "exercise": {
                    "description": "定义 Clock 类：\n- 属性：int hour, minute\n- 构造函数：Clock(int h, int m)\n- 方法：void show() 输出 \"当前时间：h:m\"\n\n输入：14 30\n输出：当前时间：14:30",
                    "template": "#include <iostream>\nusing namespace std;\n\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "14 30",
                    "sample_output": "当前时间：14:30"
                }
            }
        ]
    },
    {
        "id": 13,
        "name": "封装与访问控制",
        "phase": "第4阶段：面向对象编程",
        "steps": [
            {
                "concept": "三种访问修饰符：\n  public     — 任何地方都可以访问\n  private    — 只有类内部可以访问\n  protected  — 类和子类可以访问\n\n封装规范：属性设为 private，通过 getter/setter 访问。\n\nclass BankAccount {\nprivate:\n    double balance;  // 私有\npublic:\n    double getBalance() { return balance; }\n    void deposit(double n) { if(n>0) balance+=n; }\n};",
                "example": "#include <iostream>\n#include <string>\nusing namespace std;\n\nclass BankAccount {\nprivate:\n    string owner;\n    double balance;\n    \npublic:\n    BankAccount(string name, double initMoney)\n        : owner(name), balance(initMoney) {}\n    \n    double getBalance() { return balance; }\n    \n    void deposit(double amount) {\n        if (amount > 0) {\n            balance += amount;\n            cout << \"存款成功！余额：\" << balance << endl;\n        }\n    }\n    \n    bool withdraw(double amount) {\n        if (amount > 0 && amount <= balance) {\n            balance -= amount;\n            cout << \"取款成功！余额：\" << balance << endl;\n            return true;\n        }\n        cout << \"余额不足！\" << endl;\n        return false;\n    }\n};\n\nint main() {\n    BankAccount acc(\"小明\", 1000);\n    acc.deposit(500);  // 存款成功\n    acc.withdraw(200); // 取款成功\n    return 0;\n}",
                "exercise": {
                    "description": "定义 Temperature 类：\n- 私有属性：double celsius\n- 公有方法：\n  - void setCelsius(double c) 设置温度\n  - double toFahrenheit() 转为华氏度（F = C * 9/5 + 32）\n\n输入：30\n输出：86",
                    "template": "#include <iostream>\nusing namespace std;\n\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "30",
                    "sample_output": "86"
                }
            }
        ]
    },
    {
        "id": 14,
        "name": "继承与多态",
        "phase": "第4阶段：面向对象编程",
        "steps": [
            {
                "concept": "继承：子类获得父类的属性和方法。\n\n  class 子类 : public 父类 {\n      // 子类特有的内容\n  };\n\n调用父类构造函数：\n  子类(参数) : 父类(参数) { }\n\n三种继承方式：public / private / protected",
                "example": "#include <iostream>\n#include <string>\nusing namespace std;\n\n// 基类\nclass Animal {\npublic:\n    string name;\n    int age;\n    \n    Animal(string n, int a) : name(n), age(a) {}\n    \n    void eat() {\n        cout << name << \"正在吃东西...\" << endl;\n    }\n    \n    void sleep() {\n        cout << name << \"正在睡觉...\" << endl;\n    }\n};\n\n// 派生类\nclass Dog : public Animal {\npublic:\n    string breed;\n    \n    Dog(string n, int a, string b) \n        : Animal(n, a), breed(b) {}\n    \n    void bark() {\n        cout << name << \"汪汪叫！\" << endl;\n    }\n};\n\nint main() {\n    Dog dog(\"旺财\", 3, \"金毛\");\n    dog.eat();   // 继承自Animal\n    dog.bark();  // 自己的方法\n    return 0;\n}",
                "exercise": {
                    "description": "定义基类 Shape：\n- 保护属性：double area\n- 公有方法：void showArea() 输出\"面积：area\"\n\n定义派生类 Rectangle：\n- 属性：double width, height\n- 构造函数初始化并计算面积\n\n输入：4 7\n输出：面积：28",
                    "template": "#include <iostream>\nusing namespace std;\n\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "4 7",
                    "sample_output": "面积：28"
                }
            },
            {
                "concept": "多态：相同的接口，不同的实现。\n\n虚函数：virtual 关键字\n  virtual void speak() { ... }\n\n纯虚函数（抽象类）：\n  virtual void speak() = 0;  // 必须被重写\n\n有了纯虚函数的类叫抽象类，不能创建对象。",
                "example": "#include <iostream>\nusing namespace std;\n\n// 抽象类\nclass Shape {\npublic:\n    virtual double area() = 0;  // 纯虚函数\n    virtual void show() {\n        cout << \"面积：\" << area() << endl;\n    }\n};\n\nclass Circle : public Shape {\nprivate:\n    double r;\npublic:\n    Circle(double radius) : r(radius) {}\n    double area() override {  // 重写\n        return 3.14159 * r * r;\n    }\n};\n\nclass Rectangle : public Shape {\nprivate:\n    double w, h;\npublic:\n    Rectangle(double width, double height) : w(width), h(height) {}\n    double area() override {\n        return w * h;\n    }\n};\n\nint main() {\n    Shape* shapes[2];\n    shapes[0] = new Circle(5);\n    shapes[1] = new Rectangle(4, 6);\n    \n    for (int i = 0; i < 2; i++) {\n        shapes[i]->show();\n    }\n    return 0;\n}",
                "exercise": {
                    "description": "练习在开发环境中手动编译运行，理解多态的概念。\n\n可以先尝试写出上面的代码在自己的编译器中运行。\n\n（由于C++多态需要编译器支持，此处为思考题）\n\n请在下方写出你的代码，或者输入\"skip\"跳过。",
                    "template": "// 请尝试在本地编译器中运行多态示例代码",
                    "sample_input": "",
                    "sample_output": "面积：78.54\n面积：24"
                }
            }
        ]
    },

    # ============================================================
    # 第5阶段：STL与高级主题 (15-20课)
    # ============================================================
    {
        "id": 15,
        "name": "vector - 动态数组",
        "phase": "第5阶段：STL与高级主题",
        "steps": [
            {
                "concept": "vector 是STL中的动态数组，可以自动扩容。\n需要 #include <vector>\n\n常用操作：\n  vector<int> v;        // 创建空vector\n  v.push_back(x);       // 末尾添加\n  v.size()              // 元素个数\n  v[i]                  // 访问（不检查越界）\n  v.at(i)               // 访问（检查越界）\n  v.pop_back()          // 删除末尾\n  v.clear()             // 清空\n  v.empty()             // 是否为空",
                "example": "#include <iostream>\n#include <vector>\nusing namespace std;\n\nint main() {\n    vector<int> scores;\n    \n    scores.push_back(85);\n    scores.push_back(92);\n    scores.push_back(78);\n    \n    cout << \"人数：\" << scores.size() << endl;\n    \n    // 遍历\n    for (int i = 0; i < scores.size(); i++) {\n        cout << scores[i] << \" \";\n    }\n    cout << endl;\n    \n    // 范围for循环（C++11）\n    int sum = 0;\n    for (int s : scores) {\n        sum += s;\n    }\n    cout << \"平均分：\" << (double)sum / scores.size() << endl;\n    \n    return 0;\n}",
                "exercise": {
                    "description": "输入 n 和 n 个整数，存入 vector，输出：\n1. 所有元素（空格隔开）\n2. 最大值\n3. 最小值\n\n输入：\n5\n3 7 1 9 4\n输出：\n3 7 1 9 4\n9\n1",
                    "template": "#include <iostream>\n#include <vector>\nusing namespace std;\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "5\n3 7 1 9 4",
                    "sample_output": "3 7 1 9 4\n9\n1"
                }
            },
            {
                "concept": "vector 高级操作：\n  v.insert(pos, val)    // 插入\n  v.erase(pos)           // 删除\n  sort(v.begin(), v.end()) // 排序（需要 <algorithm>）\n  reverse(v.begin(), v.end()) // 反转\n\n迭代器遍历：\n  for (auto it = v.begin(); it != v.end(); it++) {\n      cout << *it << \" \";\n  }",
                "example": "#include <iostream>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    vector<int> v = {3, 1, 4, 1, 5, 9};\n    \n    sort(v.begin(), v.end());\n    for (int x : v) cout << x << \" \";  // 1 1 3 4 5 9\n    cout << endl;\n    \n    reverse(v.begin(), v.end());\n    for (int x : v) cout << x << \" \";  // 9 5 4 3 1 1\n    cout << endl;\n    \n    // 删除第3个\n    v.erase(v.begin() + 2);\n    cout << \"删除后：\" << v.size() << endl;\n    \n    return 0;\n}",
                "exercise": {
                    "description": "输入 n 和 n 个数，存入 vector，排序后输出。\n\n输入：\n5\n3 7 1 9 4\n输出：1 3 4 7 9\n\n提示：#include <algorithm>，sort(v.begin(), v.end())",
                    "template": "#include <iostream>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "5\n3 7 1 9 4",
                    "sample_output": "1 3 4 7 9"
                }
            }
        ]
    },
    {
        "id": 16,
        "name": "STL容器 - map与set",
        "phase": "第5阶段：STL与高级主题",
        "steps": [
            {
                "concept": "map（键值对映射）和 set（集合）是STL的关联容器。\n\nmap：\n  #include <map>\n  map<string, int> scores;\n  scores[\"张三\"] = 85;  // 插入\n  cout << scores[\"张三\"];  // 访问\n\nset：\n  #include <set>\n  set<int> s;\n  s.insert(10);      // 插入\n  s.count(10);       // 判断是否存在（0或1）\n  s.erase(10);       // 删除\n\n特点：自动排序、不重复、查找快（O(log n)）",
                "example": "#include <iostream>\n#include <map>\n#include <string>\nusing namespace std;\n\nint main() {\n    // map示例\n    map<string, int> scores;\n    scores[\"张三\"] = 85;\n    scores[\"李四\"] = 92;\n    scores[\"王五\"] = 78;\n    \n    // 遍历\n    for (auto &p : scores) {\n        cout << p.first << \": \" << p.second << endl;\n    }\n    \n    // map自动按键排序\n    \n    // set示例\n    set<int> nums = {3, 1, 4, 1, 5, 9};\n    for (int x : nums) {\n        cout << x << \" \";  // 1 3 4 5 9（去重+排序）\n    }\n    cout << endl;\n    \n    return 0;\n}",
                "exercise": {
                    "description": "用 map 统计每个数字出现的次数。\n输入 n 和 n 个整数，输出每个数字及其出现次数。\n\n输入：\n8\n1 2 2 3 3 3 4 5\n输出：\n1:1\n2:2\n3:3\n4:1\n5:1",
                    "template": "#include <iostream>\n#include <map>\nusing namespace std;\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "8\n1 2 2 3 3 3 4 5",
                    "sample_output": "1:1\n2:2\n3:3\n4:1\n5:1"
                }
            }
        ]
    },
    {
        "id": 17,
        "name": "文件操作",
        "phase": "第5阶段：STL与高级主题",
        "steps": [
            {
                "concept": "文件操作需要 #include <fstream>。\n\n写入文件：\n  ofstream fout(\"文件.txt\");\n  fout << \"内容\" << endl;\n  fout.close();\n\n读取文件：\n  ifstream fin(\"文件.txt\");\n  string line;\n  while (getline(fin, line)) {\n      cout << line << endl;\n  }\n  fin.close();\n\n检查文件是否打开：if (fin.is_open())",
                "example": "#include <iostream>\n#include <fstream>\n#include <string>\nusing namespace std;\n\nint main() {\n    // 写入\n    ofstream fout(\"test.txt\");\n    if (fout.is_open()) {\n        fout << \"Hello, File!\" << endl;\n        fout << \"第二行内容\" << endl;\n        fout.close();\n        cout << \"写入成功\" << endl;\n    }\n    \n    // 读取\n    ifstream fin(\"test.txt\");\n    string line;\n    cout << \"文件内容：\" << endl;\n    while (getline(fin, line)) {\n        cout << line << endl;\n    }\n    fin.close();\n    \n    return 0;\n}",
                "exercise": {
                    "description": "由于评测环境文件操作受限，这道题改为：\n输入一个字符串，输出\"写入成功：[字符串]\"。\n\n输入：C++ is fun\n输出：写入成功：C++ is fun",
                    "template": "#include <iostream>\n#include <string>\nusing namespace std;\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "C++ is fun",
                    "sample_output": "写入成功：C++ is fun"
                }
            }
        ]
    },
    {
        "id": 18,
        "name": "异常处理",
        "phase": "第5阶段：STL与高级主题",
        "steps": [
            {
                "concept": "异常处理让程序优雅地处理错误。\n\n  try {\n      // 可能出错的代码\n      throw 异常信息;\n  } catch (类型 变量) {\n      // 处理异常\n  } catch (...) {\n      // 捕获所有异常\n  }\n\n异常会逐层传递直到被捕获，如果一直没被捕获程序会终止。",
                "example": "#include <iostream>\nusing namespace std;\n\ndouble divide(double a, double b) {\n    if (b == 0) {\n        throw \"除数不能为0！\";\n    }\n    return a / b;\n}\n\nint main() {\n    double x, y;\n    cin >> x >> y;\n    \n    try {\n        double result = divide(x, y);\n        cout << x << \" / \" << y << \" = \" << result << endl;\n    } catch (const char* msg) {\n        cout << \"错误：\" << msg << endl;\n    }\n    \n    cout << \"程序继续运行...\" << endl;\n    return 0;\n}",
                "exercise": {
                    "description": "编写函数 mySqrt(x)，如果 x < 0 就 throw 异常。\n在 main 中调用并捕获异常。\n\n输入：-9\n输出：错误：负数不能开平方",
                    "template": "#include <iostream>\n#include <cmath>\nusing namespace std;\n\n\ndouble mySqrt(double x) {\n    if (x < 0) {\n        \n    }\n    return sqrt(x);\n}\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "-9",
                    "sample_output": "错误：负数不能开平方"
                }
            }
        ]
    },

    # ============================================================
    # 第6阶段：综合实战 (19-21课)
    # ============================================================
    {
        "id": 19,
        "name": "综合实战 - 学生管理系统",
        "phase": "第6阶段：综合实战",
        "steps": [
            {
                "concept": "综合运用学过的知识完成学生成绩管理系统。\n\n设计：\n- Student 类：学号、姓名、成绩\n- 输入学生信息\n- 计算平均分\n- 按成绩排序",
                "example": "#include <iostream>\n#include <string>\n#include <vector>\n#include <algorithm>\n#include <iomanip>\nusing namespace std;\n\nclass Student {\npublic:\n    string name;\n    int id;\n    double score;\n    \n    Student(string n, int i, double s)\n        : name(n), id(i), score(s) {}\n    \n    void display() {\n        cout << name << \" \" << id << \" \" << score << endl;\n    }\n};\n\nint main() {\n    vector<Student> students;\n    int n;\n    cin >> n;\n    \n    for (int i = 0; i < n; i++) {\n        string name;\n        int id;\n        double score;\n        cin >> name >> id >> score;\n        students.push_back(Student(name, id, score));\n    }\n    \n    // 按成绩降序排序\n    sort(students.begin(), students.end(),\n         [](const Student &a, const Student &b) {\n             return a.score > b.score;\n         });\n    \n    double sum = 0;\n    for (auto &s : students) {\n        s.display();\n        sum += s.score;\n    }\n    cout << \"平均分：\" << fixed << setprecision(1) \n         << sum / n << endl;\n    \n    return 0;\n}",
                "exercise": {
                    "description": "实现学生管理系统：\n1. 输入 n 个学生（姓名 学号 成绩）\n2. 输出所有学生信息\n3. 输出平均分（保留1位小数）\n\n输入：\n3\n张三 1001 85.5\n李四 1002 92.0\n王五 1003 78.5\n输出：\n张三 1001 85.5\n李四 1002 92.0\n王五 1003 78.5\n平均分：85.3",
                    "template": "#include <iostream>\n#include <string>\n#include <iomanip>\nusing namespace std;\n\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "3\n张三 1001 85.5\n李四 1002 92.0\n王五 1003 78.5",
                    "sample_output": "张三 1001 85.5\n李四 1002 92.0\n王五 1003 78.5\n平均分：85.3"
                }
            },
            {
                "concept": "增强功能：按成绩排序后输出。\n\n使用 sort 和 lambda 表达式：\n  sort(v.begin(), v.end(), [](类型 a, 类型 b) {\n      return a.score > b.score;  // 降序\n  });\n\n查找：遍历 vector 匹配条件。\n删除：用 erase 或重新构建 vector。",
                "example": "// 按成绩降序排序\nsort(students.begin(), students.end(),\n     [](const Student &a, const Student &b) {\n         return a.score > b.score;\n     });\n\n// 按姓名查找\nstring keyword = \"张\";\nfor (auto &s : students) {\n    if (s.name.find(keyword) != string::npos) {\n        s.display();\n    }\n}\n\n// 删除指定学号的学生\nint deleteId = 1002;\nfor (auto it = students.begin(); it != students.end(); ) {\n    if (it->id == deleteId) {\n        it = students.erase(it);\n    } else {\n        it++;\n    }\n}",
                "exercise": {
                    "description": "在上一题基础上增加排序功能，按成绩从高到低输出。\n\n输入：\n3\n张三 1001 85.5\n李四 1002 92.0\n王五 1003 78.5\n输出：\n李四 1002 92.0\n张三 1001 85.5\n王五 1003 78.5\n平均分：85.3",
                    "template": "#include <iostream>\n#include <string>\n#include <vector>\n#include <algorithm>\n#include <iomanip>\nusing namespace std;\n\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "3\n张三 1001 85.5\n李四 1002 92.0\n王五 1003 78.5",
                    "sample_output": "李四 1002 92.0\n张三 1001 85.5\n王五 1003 78.5\n平均分：85.3"
                }
            }
        ]
    }
]

PHASES_CPP = [
    "第1阶段：C++基础入门",
    "第2阶段：控制流程",
    "第3阶段：函数与指针",
    "第4阶段：面向对象编程",
    "第5阶段：STL与高级主题",
    "第6阶段：综合实战"
]
