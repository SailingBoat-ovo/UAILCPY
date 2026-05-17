# -*- coding: utf-8 -*-
# C++高级课程 - 竞赛级内容

lessons_cpp_advanced = [
    {
        "id": 20,
        "name": "模板 - 泛型编程",
        "phase": "第7阶段：C++进阶与竞赛",
        "steps": [
            {
                "concept": "模板是C++泛型编程的基础，也是竞赛中高效复用的关键。\n\n函数模板：\n  template<typename T>\n  T max(T a, T b) {\n      return a > b ? a : b;\n  }\n\n类模板：\n  template<typename T>\n  class Stack {\n      vector<T> data;\n  public:\n      void push(T v) { data.push_back(v); }\n      T pop() { T v=data.back(); data.pop_back(); return v; }\n  };\n\n模板特化：对特定类型提供不同实现\n  template<>\n  class Stack<bool> { ... };  // 特化版本",
                "example": "#include <iostream>\n#include <vector>\nusing namespace std;\n\n// 函数模板\ntemplate<typename T>\nT my_max(T a, T b) {\n    return a > b ? a : b;\n}\n\n// 类模板\ntemplate<typename T>\nclass Stack {\nprivate:\n    vector<T> data;\npublic:\n    void push(const T& v) { data.push_back(v); }\n    T pop() {\n        T v = data.back();\n        data.pop_back();\n        return v;\n    }\n    bool empty() const { return data.empty(); }\n    size_t size() const { return data.size(); }\n};\n\nint main() {\n    // 函数模板使用\n    cout << my_max(3, 5) << endl;        // 5\n    cout << my_max(3.14, 2.5) << endl;   // 3.14\n    cout << my_max(\"abc\", \"abd\") << endl; // abd\n    \n    // 类模板使用\n    Stack<int> s;\n    s.push(10);\n    s.push(20);\n    cout << s.pop() << \" \" << s.pop() << endl;  // 20 10\n    \n    Stack<string> names;\n    names.push(\"Alice\");\n    names.push(\"Bob\");\n    cout << names.pop() << endl;  // Bob\n    \n    return 0;\n}",
                "exercise": {
                    "description": "编写一个函数模板 find_max(T arr[], int n)，返回数组中的最大值。\n在 main 中分别用 int 数组和 double 数组测试。\n\n输入：5\n1 8 3 6 2\n输出：8",
                    "template": "#include <iostream>\nusing namespace std;\n\n\ntemplate<typename T>\nT find_max(T arr[], int n) {\n    \n}\n\nint main() {\n    int n;\n    cin >> n;\n    double* arr = new double[n];\n    for (int i = 0; i < n; i++) cin >> arr[i];\n    cout << find_max(arr, n) << endl;\n    delete[] arr;\n    return 0;\n}",
                    "sample_input": "5\n1 8 3 6 2",
                    "sample_output": "8"
                }
            },
            {
                "concept": "模板特化与SFINAE（竞赛高级技巧）\n\n完全特化：template<> class Class<具体类型>\n偏特化：template<typename T> class Class<T*>\n\ndecltype 和 auto 在模板中的应用：\n  template<typename T, typename U>\n  auto add(T a, U b) -> decltype(a + b) {\n      return a + b;\n  }\n\nC++11 变参模板：\n  template<typename... Args>\n  void print_all(Args... args) {\n      (cout << ... << args) << endl;  // C++17折叠表达式\n  }",
                "example": "#include <iostream>\n#include <string>\nusing namespace std;\n\n// 变参模板 - 递归展开\nvoid print() { cout << endl; }  // 终止条件\n\ntemplate<typename T, typename... Args>\nvoid print(T first, Args... rest) {\n    cout << first << \" \";\n    print(rest...);  // 递归调用\n}\n\n// C++17 折叠表达式\ntemplate<typename... Args>\nauto sum_all(Args... args) {\n    return (... + args);  // 一元左折叠\n}\n\nint main() {\n    print(1, 2.5, \"hello\", 'A');  // 1 2.5 hello A\n    \n    cout << sum_all(1, 2, 3, 4, 5) << endl;  // 15\n    cout << sum_all(1.5, 2.5, 3.0) << endl;   // 7.0\n    \n    // enable_if 示例（SFINAE）\n    // 可以用来限制模板参数类型\n    \n    return 0;\n}",
                "exercise": {
                    "description": "用变参模板实现一个 average 函数，计算任意数量参数的平均值。\n\n使用：(... + args) / sizeof...(args)\n\ncout << average(1, 2, 3, 4, 5) << endl;\ncout << average(1.5, 2.5, 3.0) << endl;\n\n（在本地编译器中测试运行）",
                    "template": "#include <iostream>\nusing namespace std;\n\ntemplate<typename... Args>\nauto average(Args... args) {\n    return (... + args) / (double)sizeof...(args);\n}\n\nint main() {\n    cout << average(1, 2, 3, 4, 5) << endl;\n    cout << average(1.5, 2.5, 3.0) << endl;\n    return 0;\n}",
                    "sample_input": "",
                    "sample_output": "3\n2.33333"
                }
            }
        ]
    },
    {
        "id": 21,
        "name": "STL算法深入",
        "phase": "第7阶段：C++进阶与竞赛",
        "steps": [
            {
                "concept": "<algorithm> 包含大量竞赛必备算法。\n\n排序相关：\n  sort(begin, end)           - 快排 O(n log n)\n  stable_sort(begin, end)     - 稳定排序\n  partial_sort(begin, mid, end) - 部分排序\n  nth_element(begin, nth, end)  - 第n大元素 O(n)\n\n查找：\n  binary_search(begin, end, val) - 二分查找\n  lower_bound(begin, end, val)   - 第一个 >= val\n  upper_bound(begin, end, val)   - 第一个 > val\n  equal_range(begin, end, val)   - 范围\n\n其他：\n  max/min/max_element/min_element\n  reverse/rotate/shuffle\n  unique（去重）\n  next_permutation（下一个排列！竞赛高频）",
                "example": "#include <iostream>\n#include <algorithm>\n#include <vector>\nusing namespace std;\n\nint main() {\n    vector<int> v = {3, 1, 4, 1, 5, 9, 2, 6};\n    \n    // nth_element：找出第3大的元素\n    nth_element(v.begin(), v.begin() + 2, v.end());\n    // 第0,1,2 是前三小（不一定有序），其余在后面\n    cout << \"第3小的数: \" << v[2] << endl;\n    \n    // 全排列（竞赛经典！）\n    vector<int> arr = {1, 2, 3};\n    sort(arr.begin(), arr.end());  // 必须先排序\n    do {\n        for (int x : arr) cout << x << \" \";\n        cout << endl;\n    } while (next_permutation(arr.begin(), arr.end()));\n    // 输出所有排列:\n    // 1 2 3\n    // 1 3 2\n    // 2 1 3\n    // ...\n    \n    // lower_bound 和 upper_bound\n    vector<int> sorted = {1, 2, 2, 2, 3, 4, 5};\n    auto l = lower_bound(sorted.begin(), sorted.end(), 2);\n    auto u = upper_bound(sorted.begin(), sorted.end(), 2);\n    cout << \"2出现次数: \" << u - l << endl;  // 3\n    \n    return 0;\n}",
                "exercise": {
                    "description": "输入 n 和 n 个整数，用 next_permutation 输出它们的下一个排列。\n\n输入：\n3\n1 3 2\n输出：2 1 3\n\n提示：先检查是否有下一个排列（函数返回true）",
                    "template": "#include <iostream>\n#include <algorithm>\n#include <vector>\nusing namespace std;\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "3\n1 3 2",
                    "sample_output": "2 1 3"
                }
            }
        ]
    },
    {
        "id": 22,
        "name": "智能指针与内存管理",
        "phase": "第7阶段：C++进阶与竞赛",
        "steps": [
            {
                "concept": "智能指针自动管理内存，避免泄漏。\n需要 #include <memory>\n\nunique_ptr：独占所有权\n  unique_ptr<int> p = make_unique<int>(42);\n  // 不能拷贝，只能移动\n  auto q = move(p);  // 所有权转移\n\nshared_ptr：共享所有权（引用计数）\n  shared_ptr<int> p = make_shared<int>(42);\n  auto q = p;  // 引用计数+1\n  // 当最后一个 shared_ptr 销毁时释放内存\n\nweak_ptr：弱引用（不增加引用计数）\n  weak_ptr<int> wp = p;\n  // 用于打破循环引用\n\n现代C++应避免使用 new/delete，使用智能指针。",
                "example": "#include <iostream>\n#include <memory>\nusing namespace std;\n\nclass Node {\npublic:\n    int value;\n    Node(int v) : value(v) {\n        cout << \"Node \" << value << \" created\" << endl;\n    }\n    ~Node() {\n        cout << \"Node \" << value << \" destroyed\" << endl;\n    }\n};\n\nint main() {\n    // unique_ptr\n    {\n        auto p = make_unique<Node>(10);\n        cout << \"值: \" << p->value << endl;\n        // 离开作用域自动释放\n    }\n    \n    cout << \"---\" << endl;\n    \n    // shared_ptr\n    {\n        shared_ptr<Node> p1 = make_shared<Node>(20);\n        {\n            shared_ptr<Node> p2 = p1;\n            cout << \"引用计数: \" << p2.use_count() << endl;\n        }\n        cout << \"引用计数: \" << p1.use_count() << endl;\n    }\n    \n    cout << \"---\" << endl;\n    \n    // weak_ptr（用于打破循环引用）\n    shared_ptr<Node> sp = make_shared<Node>(30);\n    weak_ptr<Node> wp = sp;\n    cout << \"weak 过期? \" << wp.expired() << endl;\n    if (auto locked = wp.lock()) {  // 提升为shared\n        cout << \"locked: \" << locked->value << endl;\n    }\n    \n    return 0;\n}",
                "exercise": {
                    "description": "用 unique_ptr 重写动态内存分配。\n创建一个 unique_ptr<int>，赋值为输入的值，输出后自动释放。\n\n输入：42\n输出：42\n\n提示：auto p = make_unique<int>();",
                    "template": "#include <iostream>\n#include <memory>\nusing namespace std;\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "42",
                    "sample_output": "42"
                }
            }
        ]
    },
    {
        "id": 23,
        "name": "Lambda与函数对象",
        "phase": "第7阶段：C++进阶与竞赛",
        "steps": [
            {
                "concept": "Lambda 表达式是C++11引入的匿名函数，竞赛中广泛用于STL算法的自定义操作。\n\n语法：\n  [捕获列表](参数列表) -> 返回类型 { 函数体 }\n\n捕获方式：\n  []        - 不捕获任何变量\n  [x, &y]   - 按值捕获x，按引用捕获y\n  [=]       - 按值捕获所有外部变量\n  [&]       - 按引用捕获所有外部变量\n  [=, &x]   - 按值捕获所有，但x按引用\n\n从C++14开始支持泛型lambda和捕获初始化。",
                "example": "#include <iostream>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    vector<int> nums = {5, 2, 8, 1, 9, 3};\n    \n    // 按绝对值排序\n    sort(nums.begin(), nums.end(),\n         [](int a, int b) { return abs(a) < abs(b); });\n    \n    // 带捕获的lambda\n    int threshold = 3;\n    auto count = count_if(nums.begin(), nums.end(),\n                          [threshold](int x) { return x > threshold; });\n    cout << \"大于\" << threshold << \"的数有\" << count << \"个\" << endl;\n    \n    // 泛型lambda（C++14）\n    auto add = [](auto a, auto b) { return a + b; };\n    cout << add(3, 5) << endl;       // 8\n    cout << add(1.5, 2.5) << endl;   // 4.0\n    \n    // 捕获初始化（C++14）\n    auto generator = [n = 0]() mutable { return n++; };\n    cout << generator() << endl;  // 0\n    cout << generator() << endl;  // 1\n    cout << generator() << endl;  // 2\n    \n    // lambda实现递归（需要std::function）\n    function<int(int)> fib = [&fib](int n) {\n        return n <= 1 ? n : fib(n-1) + fib(n-2);\n    };\n    cout << \"fib(10) = \" << fib(10) << endl;  // 55\n    \n    return 0;\n}",
                "exercise": {
                    "description": "用lambda表达式作为排序的 key，将输入的整数按绝对值从大到小排序后输出。\n\n输入：-5 3 -8 1 2\n输出：-8 -5 3 2 1\n\n提示：sort(v.begin(), v.end(), [](int a, int b) { ... });",
                    "template": "#include <iostream>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "-5 3 -8 1 2",
                    "sample_output": "-8 -5 3 2 1"
                }
            }
        ]
    },
    {
        "id": 24,
        "name": "运算符重载",
        "phase": "第7阶段：C++进阶与竞赛",
        "steps": [
            {
                "concept": "运算符重载允许自定义类型的运算符行为，竞赛中常用于自定义数据结构的比较和运算。\n\n可重载的运算符：\n  算术：+ - * / %\n  比较：== != < > <= >=\n  赋值：= += -= 等\n  流：<< >>\n  下标：[]\n  函数调用：()\n  自增自减：++ --\n\n语法：\n  返回类型 operator 符号(参数列表) { ... }\n\n注意：:: . .* ?: 不能重载\n建议：保持运算符的语义，不要重载成奇怪的行为。",
                "example": "#include <iostream>\nusing namespace std;\n\nclass Fraction {\nprivate:\n    int num, den;  // 分子/分母\npublic:\n    Fraction(int n, int d) : num(n), den(d) { simplify(); }\n    \n    void simplify() {\n        int g = gcd(abs(num), abs(den));\n        num /= g; den /= g;\n        if (den < 0) { num = -num; den = -den; }\n    }\n    \n    static int gcd(int a, int b) {\n        return b == 0 ? a : gcd(b, a % b);\n    }\n    \n    // 重载 + \n    Fraction operator+(const Fraction& other) const {\n        return Fraction(num * other.den + other.num * den,\n                       den * other.den);\n    }\n    \n    // 重载 ==\n    bool operator==(const Fraction& other) const {\n        return num == other.num && den == other.den;\n    }\n    \n    // 重载 << （必须用友元或全局函数）\n    friend ostream& operator<<(ostream& os, const Fraction& f) {\n        os << f.num;\n        if (f.den != 1) os << \"/\" << f.den;\n        return os;\n    }\n};\n\nint main() {\n    Fraction a(1, 2), b(1, 3);\n    cout << a << \" + \" << b << \" = \" << a + b << endl;  // 5/6\n    \n    Fraction c(2, 4);  // 会自动化简为 1/2\n    cout << c << \" == \" << a << \" ? \" << (c == a) << endl;  // 1 (true)\n    \n    return 0;\n}",
                "exercise": {
                    "description": "为 Point 类重载 < 运算符，按到原点的距离比较大小。\n然后输入 n 个点，按距离从小到大排序输出。\n\n输入：\n3\n3 4\n1 1\n0 5\n输出：\n(1,1)\n(3,4)\n(0,5)\n\n提示：距离 = sqrt(x*x + y*y)",
                    "template": "#include <iostream>\n#include <vector>\n#include <algorithm>\n#include <cmath>\nusing namespace std;\n\nclass Point {\npublic:\n    int x, y;\n    Point(int a, int b) : x(a), y(b) {}\n    double dist() const { return sqrt(x*x + y*y); }\n    \n    \n    \n    friend ostream& operator<<(ostream& os, const Point& p) {\n        os << \"(\" << p.x << \",\" << p.y << \")\";\n        return os;\n    }\n};\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "3\n3 4\n1 1\n0 5",
                    "sample_output": "(1,1)\n(3,4)\n(0,5)"
                }
            }
        ]
    },
    {
        "id": 25,
        "name": "STL数据结构深入",
        "phase": "第7阶段：C++进阶与竞赛",
        "steps": [
            {
                "concept": "竞赛中常用但容易被忽略的STL容器。\n\npriority_queue（优先队列/堆）：\n  #include <queue>\n  priority_queue<int> pq;          // 大顶堆\n  priority_queue<int, vector<int>, greater<int>> pq; // 小顶堆\n  pq.push(x); pq.pop(); pq.top();\n\nunordered_map / unordered_set（哈希表，O(1)操作）：\n  #include <unordered_map>\n  unordered_map<string, int> um;\n  um[key] = value;\n  um.count(key)  // 检查是否存在\n\nmultiset / multimap（允许重复的set/map）：\n  #include <set>\n  multiset<int> ms;\n  ms.count(x)  // 统计出现次数\n\nbitset（位集合，高效位运算）：\n  #include <bitset>\n  bitset<1000> bits;\n  bits.set(i); bits.reset(i); bits.test(i);",
                "example": "#include <iostream>\n#include <queue>\n#include <unordered_map>\n#include <string>\n#include <bitset>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    // 小顶堆：取最小的k个数\n    priority_queue<int, vector<int>, greater<int>> min_heap;\n    vector<int> nums = {3, 1, 4, 1, 5, 9, 2, 6};\n    for (int x : nums) min_heap.push(x);\n    cout << \"从小到大: \";\n    while (!min_heap.empty()) {\n        cout << min_heap.top() << \" \";\n        min_heap.pop();\n    }\n    cout << endl;\n    \n    // unordered_map 统计频率\n    unordered_map<string, int> freq;\n    vector<string> words = {\"apple\", \"banana\", \"apple\", \"orange\", \"banana\", \"apple\"};\n    for (const string& w : words) freq[w]++;\n    for (auto& p : freq)\n        cout << p.first << \": \" << p.second << endl;\n    \n    // bitset\n    bitset<10> bs;\n    bs.set(0); bs.set(3); bs.set(7);\n    cout << \"bitset: \" << bs << endl;\n    cout << \"bit 3: \" << bs.test(3) << endl;\n    cout << \"bit 1: \" << bs.test(1) << endl;\n    \n    return 0;\n}",
                "exercise": {
                    "description": "用 priority_queue（小顶堆）找出 n 个数中最小的 k 个。\n\n输入：\n6 3\n5 2 8 1 9 3\n输出：1 2 3\n\n提示：先全部入堆，然后依次pop",
                    "template": "#include <iostream>\n#include <queue>\n#include <vector>\nusing namespace std;\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "6 3\n5 2 8 1 9 3",
                    "sample_output": "1 2 3"
                }
            }
        ]
    },
    {
        "id": 26,
        "name": "C++17/20新特性",
        "phase": "第7阶段：C++进阶与竞赛",
        "steps": [
            {
                "concept": "现代C++（C++17/20）引入了许多简化代码的特性，竞赛中越来越常用。\n\nC++17 关键特性：\n  if constexpr        - 编译期条件分支（模板中常用）\n  structured bindings - 结构体绑定（解包）\n  auto [a, b] = func();\n  fold expressions    - 折叠表达式\n  string_view         - 轻量字符串视图（不拷贝）\n  optional            - 可选值（可能有也可能没有）\n  variant             - 类型安全的联合体\n\nC++20 关键特性：\n  concepts            - 概念（约束模板参数）\n  ranges              - 范围库（函数式风格）\n  coroutines          - 协程\n  spaceship <=>       - 三向比较运算符\n  format              - 格式化输出（类似Python）",
                "example": "#include <iostream>\n#include <tuple>\n#include <string>\n#include <optional>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\n// C++17 结构化绑定\ntuple<string, int, double> get_student() {\n    return {\"张三\", 18, 85.5};\n}\n\n// optional：可能失败的函数\noptional<int> safe_divide(int a, int b) {\n    if (b == 0) return nullopt;\n    return a / b;\n}\n\nint main() {\n    // 结构化绑定\n    auto [name, age, score] = get_student();\n    cout << name << \" \" << age << \" \" << score << endl;\n    \n    // 遍历map时特别方便\n    // for (auto& [key, value] : my_map) { ... }\n    \n    // optional\n    auto result = safe_divide(10, 3);\n    if (result.has_value()) {\n        cout << \"10/3 = \" << result.value() << endl;\n    }\n    \n    auto bad = safe_divide(10, 0);\n    cout << \"10/0 = \" << bad.value_or(-1) << endl;  // -1\n    \n    // if constexpr（模板中特别有用）\n    // template<typename T>\n    // auto process(T v) {\n    //     if constexpr (is_integral_v<T>)\n    //         return v + 1;\n    //     else\n    //         return v + 0.5;\n    // }\n    \n    return 0;\n}",
                "exercise": {
                    "description": "用结构化绑定（C++17）实现：\n编写函数返回 tuple<string, int>，在 main 中用 auto [name, age] 接收。\n\n函数返回：(\"小明\", 18)\n\n（注意：编译器需要支持C++17，用 -std=c++17 编译）",
                    "template": "#include <iostream>\n#include <tuple>\n#include <string>\nusing namespace std;\n\ntuple<string, int> get_info() {\n    return {\"小明\", 18};\n}\n\nint main() {\n    \n    return 0;\n}",
                    "sample_input": "",
                    "sample_output": "小明 18"
                }
            }
        ]
    },
    {
        "id": 27,
        "name": "竞赛算法 - 动态规划入门",
        "phase": "第7阶段：C++进阶与竞赛",
        "steps": [
            {
                "concept": "动态规划（DP）是竞赛中最核心的算法之一。\n\n核心思想：将大问题分解为小问题，记录小问题的解避免重复计算。\n\nDP三要素：\n1. 状态定义：dp[i] 表示什么？\n2. 状态转移：dp[i] = f(dp[i-1], dp[i-2], ...)\n3. 初始条件：base case\n\n经典问题：\n• 斐波那契数列\n• 爬楼梯（一次1或2步）\n• 最大子数组和\n• 0-1背包问题\n• 最长公共子序列（LCS）",
                "example": "#include <iostream>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\n// 爬楼梯问题：每次可以爬1或2阶，到n阶有多少种方法\nint climb_stairs(int n) {\n    if (n <= 2) return n;\n    vector<int> dp(n + 1, 0);\n    dp[1] = 1;  // 1阶：1种方法\n    dp[2] = 2;  // 2阶：2种方法（1+1 或 2）\n    for (int i = 3; i <= n; i++) {\n        dp[i] = dp[i-1] + dp[i-2];  // 从i-1走1阶 或 从i-2走2阶\n    }\n    return dp[n];\n}\n\n// 最大子数组和（Kadane算法）\nint max_subarray(vector<int>& nums) {\n    int cur = 0, best = nums[0];\n    for (int x : nums) {\n        cur = max(x, cur + x);  // 要么重新开始，要么累加\n        best = max(best, cur);\n    }\n    return best;\n}\n\n// 0-1背包问题\nint knapsack(int W, vector<int>& wt, vector<int>& val, int n) {\n    vector<vector<int>> dp(n+1, vector<int>(W+1, 0));\n    for (int i = 1; i <= n; i++) {\n        for (int w = 1; w <= W; w++) {\n            if (wt[i-1] <= w)\n                dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w]);\n            else\n                dp[i][w] = dp[i-1][w];\n        }\n    }\n    return dp[n][W];\n}\n\nint main() {\n    cout << \"10阶楼梯: \" << climb_stairs(10) << endl;  // 89\n    \n    vector<int> nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};\n    cout << \"最大子数组和: \" << max_subarray(nums) << endl;  // 6\n    \n    vector<int> wt = {2, 3, 4, 5};\n    vector<int> val = {3, 4, 5, 6};\n    cout << \"0-1背包(容量5): \" << knapsack(5, wt, val, 4) << endl;  // 7\n    \n    return 0;\n}",
                "exercise": {
                    "description": "使用动态规划，求第 n 个斐波那契数。\n要求用 O(n) 时间和 O(1) 空间（只用两个变量，不用数组）。\n\nF(1)=1, F(2)=1, F(n)=F(n-1)+F(n-2)\n\n输入：10\n输出：55",
                    "template": "#include <iostream>\nusing namespace std;\n\nint fib(int n) {\n    \n}\n\nint main() {\n    int n;\n    cin >> n;\n    cout << fib(n) << endl;\n    return 0;\n}",
                    "sample_input": "10",
                    "sample_output": "55"
                }
            }
        ]
    }
]

PHASES_CPP_ADVANCED = ["第7阶段：C++进阶与竞赛"]
