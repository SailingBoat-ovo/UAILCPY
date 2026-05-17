# -*- coding: utf-8 -*-
# C++ V3 完全体补全 - STL高级/图论/算法/并发/设计模式/项目

lessons_cpp_v3 = [

    # ============================================================
    # 第8阶段：高级STL与实用技巧
    # ============================================================
    {
        "id": 28,
        "name": "stringstream - 字符串流处理",
        "phase": "第8阶段：高级STL与实用技巧",
        "steps": [
            {
                "concept": "stringstream 可以把字符串当作流来处理，非常实用。\n需要 #include <sstream>\n\n  #include <sstream>\n  \n  // 字符串分割\n  string s = \"1 2 3 4 5\";\n  stringstream ss(s);\n  int num;\n  while (ss >> num) {\n      cout << num << \" \";\n  }\n  \n  // 类型转换\n  stringstream ss2;\n  ss2 << 123 << \" \" << 3.14 << \" \" << true;\n  string result = ss2.str();  // \"123 3.14 1\"\n  \n  // 格式化拼接\n  stringstream ss3;\n  ss3 << \"Name: \" << \"张三\" << \", Age: \" << 18;\n  string info = ss3.str();",
                "example": "#include <iostream>\n#include <sstream>\n#include <string>\n#include <vector>\nusing namespace std;\n\nint main() {\n    // 字符串分割为整数\n    string input = \"10 20 30 40 50\";\n    stringstream ss(input);\n    \n    vector<int> nums;\n    int num;\n    while (ss >> num) {\n        nums.push_back(num);\n    }\n    \n    cout << \"读取了 \" << nums.size() << \" 个数:\";\n    for (int n : nums) cout << \" \" << n;\n    cout << endl;\n    \n    // 拼接字符串\n    stringstream builder;\n    builder << \"姓名:\" << \"学生A\" << \", \";\n    builder << \"分数:\" << 95;\n    string info = builder.str();\n    cout << info << endl;\n    \n    // 解析逗号分隔\n    string csv = \"张三,85,李四,92,王五,78\";\n    stringstream csv_ss(csv);\n    string token;\n    while (getline(csv_ss, token, ',')) {\n        cout << token << \" \";\n    }\n    cout << endl;\n    \n    return 0;\n}",
                "exercise": {
                    "description": "输入一行用逗号分隔的整数，用 stringstream 解析并求和。\n\n输入：1,2,3,4,5\n输出：15\n\n提示：用 getline(ss, token, ',')",
                    "template": "#include <iostream>\n#include <sstream>\n#include <string>\nusing namespace std;\n\nint main() {\n    string line;\n    getline(cin, line);\n    stringstream ss(line);\n    \n    return 0;\n}",
                    "sample_input": "1,2,3,4,5",
                    "sample_output": "15"
                }
            }
        ]
    },
    {
        "id": 29,
        "name": "tuple与pair - 多值返回",
        "phase": "第8阶段：高级STL与实用技巧",
        "steps": [
            {
                "concept": "pair 和 tuple 用于组合多个值。\n\npair：两个值\n  #include <utility>\n  pair<string, int> p = {\"张三\", 18};\n  cout << p.first << \" \" << p.second;\n\ntuple：任意多个值（C++11）\n  #include <tuple>\n  tuple<string, int, double> t = {\"张三\", 18, 85.5};\n  cout << get<0>(t) << \" \" << get<1>(t);\n\n结构化绑定（C++17）：\n  auto [name, age, score] = t;",
                "example": "#include <iostream>\n#include <tuple>\n#include <string>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\n// 返回多个值\ntuple<string, int, double> get_student() {\n    return {\"张三\", 18, 85.5};\n}\n\nint main() {\n    // C++11 方式\n    auto student = get_student();\n    cout << get<0>(student) << \" \" \n         << get<1>(student) << \" \" \n         << get<2>(student) << endl;\n    \n    // C++17 结构化绑定\n    auto [name, age, score] = get_student();\n    cout << name << \" \" << age << \" \" << score << endl;\n    \n    // pair 用于map遍历\n    vector<pair<string, int>> scores = {\n        {\"张三\", 85}, {\"李四\", 92}, {\"王五\", 78}\n    };\n    \n    sort(scores.begin(), scores.end(),\n         [](const auto& a, const auto& b) {\n             return a.second > b.second;\n         });\n    \n    for (auto [name, score] : scores) {\n        cout << name << \": \" << score << endl;\n    }\n    \n    return 0;\n}",
                "exercise": {
                    "description": "输入两个点的坐标 (x1,y1) 和 (x2,y2)，用 pair<int,int> 存储。\n计算两点之间的曼哈顿距离 |x1-x2| + |y1-y2|。\n\n输入：0 0 3 4\n输出：7\n\n提示：用 make_pair 或 {} 创建pair",
                    "template": "#include <iostream>\n#include <utility>\n#include <cmath>\nusing namespace std;\n\nint main() {\n    int x1, y1, x2, y2;\n    cin >> x1 >> y1 >> x2 >> y2;\n    \n    \n    \n    return 0;\n}",
                    "sample_input": "0 0 3 4",
                    "sample_output": "7"
                }
            }
        ]
    },
    {
        "id": 30,
        "name": "chrono - 时间与计时",
        "phase": "第8阶段：高级STL与实用技巧",
        "steps": [
            {
                "concept": "chrono 库用于时间测量和日期处理。\n需要 #include <chrono>\n\n  #include <chrono>\n  using namespace chrono;\n  \n  // 计时\n  auto start = high_resolution_clock::now();\n  // ... 要计时的代码\n  auto end = high_resolution_clock::now();\n  auto duration = duration_cast<milliseconds>(end - start);\n  cout << \"耗时: \" << duration.count() << \"ms\";\n  \n  // 时间点\n  auto now = system_clock::now();\n  time_t tt = system_clock::to_time_t(now);\n  cout << ctime(&tt);  // 当前时间\n\n休眠：\n  #include <thread>\n  this_thread::sleep_for(chrono::seconds(1));",
                "example": "#include <iostream>\n#include <chrono>\n#include <thread>\n#include <vector>\n#include <algorithm>\nusing namespace std;\nusing namespace chrono;\n\nint main() {\n    // 计时测试\n    auto start = high_resolution_clock::now();\n    \n    // 排序测试\n    vector<int> v(100000);\n    for (int i = 0; i < 100000; i++) {\n        v[i] = rand();\n    }\n    sort(v.begin(), v.end());\n    \n    auto end = high_resolution_clock::now();\n    auto ms = duration_cast<milliseconds>(end - start).count();\n    auto us = duration_cast<microseconds>(end - start).count();\n    \n    cout << \"排序 100000 个整数:\" << endl;\n    cout << \"  耗时: \" << ms << \" 毫秒\" << endl;\n    cout << \"  精确: \" << us << \" 微秒\" << endl;\n    \n    // 当前时间\n    auto now = system_clock::now();\n    time_t t = system_clock::to_time_t(now);\n    cout << \"当前时间: \" << ctime(&t);\n    \n    // 休眠\n    cout << \"等待1秒...\" << endl;\n    this_thread::sleep_for(milliseconds(1000));\n    cout << \"完成!\" << endl;\n    \n    return 0;\n}",
                "exercise": {
                    "description": "用 chrono 测量 for 循环从 1 累加到 1000000 的耗时。\n输出耗时（毫秒）。\n\n代码模板已提供模板结构。",
                    "template": "#include <iostream>\n#include <chrono>\nusing namespace std;\nusing namespace chrono;\n\nint main() {\n    auto start = high_resolution_clock::now();\n    \n    long long sum = 0;\n    for (int i = 1; i <= 1000000; i++) {\n        sum += i;\n    }\n    \n    auto end = high_resolution_clock::now();\n    auto ms = duration_cast<milliseconds>(end - start).count();\n    \n    cout << ms << endl;\n    return 0;\n}",
                    "sample_input": "",
                    "sample_output": "0"
                }
            }
        ]
    },

    # ============================================================
    # 第9阶段：图论与数据结构
    # ============================================================
    {
        "id": 31,
        "name": "图论基础 - 邻接表与DFS",
        "phase": "第9阶段：图论与数据结构",
        "steps": [
            {
                "concept": "图是竞赛核心内容。用邻接表（vector<vector<int>>）表示图。\n\n  #include <vector>\n  vector<vector<int>> graph(n + 1);  // 1-based\n  \n  // 添加无向边\n  graph[u].push_back(v);\n  graph[v].push_back(u);\n\nDFS（深度优先搜索）：\n  void dfs(int u, vector<bool>& visited) {\n      visited[u] = true;\n      for (int v : graph[u]) {\n          if (!visited[v]) {\n              dfs(v, visited);\n          }\n      }\n  }\n\nBFS（广度优先搜索，找最短路径）：\n  #include <queue>\n  void bfs(int start) {\n      queue<int> q;\n      vector<bool> visited(n + 1);\n      visited[start] = true;\n      q.push(start);\n      while (!q.empty()) {\n          int u = q.front(); q.pop();\n          for (int v : graph[u]) {\n              if (!visited[v]) {\n                  visited[v] = true;\n                  q.push(v);\n              }\n          }\n      }\n  }",
                "example": "#include <iostream>\n#include <vector>\n#include <queue>\nusing namespace std;\n\nconst int N = 1005;\nvector<int> graph[N];\nbool visited[N];\n\nvoid dfs(int u) {\n    visited[u] = true;\n    cout << u << \" \";\n    for (int v : graph[u]) {\n        if (!visited[v]) {\n            dfs(v);\n        }\n    }\n}\n\nvoid bfs(int start) {\n    queue<int> q;\n    fill(visited, visited + N, false);\n    \n    visited[start] = true;\n    q.push(start);\n    \n    while (!q.empty()) {\n        int u = q.front(); q.pop();\n        cout << u << \" \";\n        for (int v : graph[u]) {\n            if (!visited[v]) {\n                visited[v] = true;\n                q.push(v);\n            }\n        }\n    }\n}\n\nint main() {\n    int n = 5;  // 节点数\n    \n    // 添加边\n    graph[1].push_back(2); graph[1].push_back(3);\n    graph[2].push_back(1); graph[2].push_back(4);\n    graph[3].push_back(1); graph[3].push_back(5);\n    graph[4].push_back(2);\n    graph[5].push_back(3);\n    \n    cout << \"DFS: \";\n    dfs(1);\n    cout << endl;\n    \n    cout << \"BFS: \";\n    bfs(1);\n    cout << endl;\n    \n    return 0;\n}",
                "exercise": {
                    "description": "实现 BFS 遍历图。输入节点数 n、边数 m 和 m 条边，从节点1开始BFS。\n\n输入：\n5 4\n1 2\n1 3\n2 4\n3 5\n输出：1 2 3 4 5\n\n提示：queue<int>，vector<vector<int>> graph(n+1)",
                    "template": "#include <iostream>\n#include <vector>\n#include <queue>\nusing namespace std;\n\nint main() {\n    int n, m;\n    cin >> n >> m;\n    \n    vector<vector<int>> graph(n + 1);\n    for (int i = 0; i < m; i++) {\n        int u, v;\n        cin >> u >> v;\n        graph[u].push_back(v);\n        graph[v].push_back(u);\n    }\n    \n    \n    \n    return 0;\n}",
                    "sample_input": "5 4\n1 2\n1 3\n2 4\n3 5",
                    "sample_output": "1 2 3 4 5"
                }
            }
        ]
    },
    {
        "id": 32,
        "name": "最短路径 - Dijkstra算法",
        "phase": "第9阶段：图论与数据结构",
        "steps": [
            {
                "concept": "Dijkstra 算法求单源最短路径（边权非负）。\n\n核心：用优先队列每次取距离最小的节点。\n\n  #include <queue>\n  using P = pair<int, int>;  // (距离, 节点)\n  priority_queue<P, vector<P>, greater<P>> pq;\n  \n  vector<int> dist(n + 1, INF);\n  dist[start] = 0;\n  pq.push({0, start});\n  \n  while (!pq.empty()) {\n      auto [d, u] = pq.top(); pq.pop();\n      if (d > dist[u]) continue;  // 过期数据\n      for (auto [v, w] : graph[u]) {\n          if (dist[u] + w < dist[v]) {\n              dist[v] = dist[u] + w;\n              pq.push({dist[v], v});\n          }\n      }\n  }\n\n时间复杂度 O((V+E)logV)",
                "example": "#include <iostream>\n#include <vector>\n#include <queue>\n#include <climits>\nusing namespace std;\n\nconst int INF = INT_MAX / 2;\n\nint main() {\n    int n = 5;  // 节点数\n    \n    // 邻接表（带权图）\n    vector<vector<pair<int, int>>> graph(n + 1);\n    \n    // 添加带权边\n    graph[1].push_back({2, 2});\n    graph[1].push_back({3, 4});\n    graph[2].push_back({3, 1});\n    graph[2].push_back({4, 7});\n    graph[3].push_back({5, 3});\n    graph[4].push_back({5, 1});\n    \n    // Dijkstra\n    vector<int> dist(n + 1, INF);\n    dist[1] = 0;\n    \n    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;\n    pq.push({0, 1});\n    \n    while (!pq.empty()) {\n        auto [d, u] = pq.top(); pq.pop();\n        if (d > dist[u]) continue;\n        \n        for (auto [v, w] : graph[u]) {\n            if (dist[u] + w < dist[v]) {\n                dist[v] = dist[u] + w;\n                pq.push({dist[v], v});\n            }\n        }\n    }\n    \n    for (int i = 1; i <= n; i++) {\n        cout << \"1->\" << i << \" = \" << dist[i] << endl;\n    }\n    \n    return 0;\n}",
                "exercise": {
                    "description": "Dijkstra 算法练习。\n给定 n 个节点和 m 条带权无向边，求从节点 1 到节点 n 的最短距离。\n\n输入：\n5 6\n1 2 2\n1 3 4\n2 3 1\n2 4 7\n3 5 3\n4 5 1\n输出：6\n\n（此题为理解题，在本地编译器中运行）",
                    "template": "#include <iostream>\n#include <vector>\n#include <queue>\n#include <climits>\nusing namespace std;\n\nconst int INF = INT_MAX / 2;\n\nint main() {\n    int n, m;\n    cin >> n >> m;\n    \n    vector<vector<pair<int,int>>> graph(n + 1);\n    for (int i = 0; i < m; i++) {\n        int u, v, w;\n        cin >> u >> v >> w;\n        graph[u].push_back({v, w});\n        graph[v].push_back({u, w});\n    }\n    \n    vector<int> dist(n + 1, INF);\n    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;\n    \n    dist[1] = 0;\n    pq.push({0, 1});\n    \n    while (!pq.empty()) {\n        auto [d, u] = pq.top(); pq.pop();\n        if (d > dist[u]) continue;\n        for (auto [v, w] : graph[u]) {\n            if (dist[u] + w < dist[v]) {\n                dist[v] = dist[u] + w;\n                pq.push({dist[v], v});\n            }\n        }\n    }\n    \n    cout << dist[n] << endl;\n    return 0;\n}",
                    "sample_input": "5 6\n1 2 2\n1 3 4\n2 3 1\n2 4 7\n3 5 3\n4 5 1",
                    "sample_output": "6"
                }
            }
        ]
    },
    {
        "id": 33,
        "name": "并查集 - 高效集合操作",
        "phase": "第9阶段：图论与数据结构",
        "steps": [
            {
                "concept": "并查集（Union-Find / Disjoint Set）用于高效管理不相交集合。\n竞赛中使用频率极高！\n\n  class UnionFind {\n      vector<int> parent, rank;\n  public:\n      UnionFind(int n) : parent(n), rank(n, 0) {\n          for (int i = 0; i < n; i++) parent[i] = i;\n      }\n      \n      int find(int x) {  // 路径压缩\n          if (parent[x] != x)\n              parent[x] = find(parent[x]);\n          return parent[x];\n      }\n      \n      void unite(int x, int y) {  // 按秩合并\n          int px = find(x), py = find(y);\n          if (px == py) return;\n          if (rank[px] < rank[py])\n              parent[px] = py;\n          else if (rank[px] > rank[py])\n              parent[py] = px;\n          else {\n              parent[py] = px;\n              rank[px]++;\n          }\n      }\n      \n      bool same(int x, int y) {\n          return find(x) == find(y);\n      }\n  };\n\n时间复杂度：近乎 O(1)（阿克曼函数的反函数）",
                "example": "#include <iostream>\n#include <vector>\nusing namespace std;\n\nclass UnionFind {\nprivate:\n    vector<int> parent, rank;\npublic:\n    UnionFind(int n) : parent(n), rank(n, 0) {\n        for (int i = 0; i < n; i++) parent[i] = i;\n    }\n    \n    int find(int x) {\n        if (parent[x] != x)\n            parent[x] = find(parent[x]);  // 路径压缩\n        return parent[x];\n    }\n    \n    void unite(int x, int y) {\n        int px = find(x), py = find(y);\n        if (px == py) return;\n        if (rank[px] < rank[py])\n            parent[px] = py;\n        else if (rank[px] > rank[py])\n            parent[py] = px;\n        else {\n            parent[py] = px;\n            rank[px]++;\n        }\n    }\n    \n    int count_sets() {\n        int count = 0;\n        for (int i = 0; i < parent.size(); i++)\n            if (parent[i] == i) count++;\n        return count;\n    }\n};\n\nint main() {\n    // 6个人，3个关系对\n    UnionFind uf(6);\n    \n    uf.unite(0, 1);  // 朋友关系\n    uf.unite(2, 3);\n    uf.unite(4, 5);\n    \n    cout << \"0和1是朋友? \" << uf.same(0, 1) << endl;  // 1\n    cout << \"0和2是朋友? \" << uf.same(0, 2) << endl;  // 0\n    cout << \"朋友圈数量: \" << uf.count_sets() << endl;  // 3\n    \n    // 合并朋友圈\n    uf.unite(1, 2);\n    cout << \"合并后朋友圈数量: \" << uf.count_sets() << endl;  // 2\n    \n    return 0;\n}",
                "exercise": {
                    "description": "用并查集判断两个节点是否在同一个集合中。\n输入 n（人数）, m（关系数），接着 m 行每行两个朋友。\n然后输入 q 个查询，每行两个节点，输出\"Yes\"或\"No\"。\n\n输入：\n5 3\n1 2\n2 3\n4 5\n2\n1 3\n1 4\n输出：\nYes\nNo",
                    "template": "#include <iostream>\n#include <vector>\nusing namespace std;\n\nclass UnionFind {\npublic:\n    vector<int> parent;\n    UnionFind(int n) {\n        parent.resize(n + 1);\n        for (int i = 1; i <= n; i++) parent[i] = i;\n    }\n    int find(int x) {\n        \n    }\n    void unite(int x, int y) {\n        \n    }\n    bool same(int x, int y) {\n        \n    }\n};\n\nint main() {\n    int n, m;\n    cin >> n >> m;\n    UnionFind uf(n);\n    for (int i = 0; i < m; i++) {\n        int a, b;\n        cin >> a >> b;\n        uf.unite(a, b);\n    }\n    int q;\n    cin >> q;\n    while (q--) {\n        int a, b;\n        cin >> a >> b;\n        cout << (uf.same(a, b) ? \"Yes\" : \"No\") << endl;\n    }\n    return 0;\n}",
                    "sample_input": "5 3\n1 2\n2 3\n4 5\n2\n1 3\n1 4",
                    "sample_output": "Yes\nNo"
                }
            }
        ]
    },

    # ============================================================
    # 第10阶段：高级算法
    # ============================================================
    {
        "id": 34,
        "name": "贪心算法",
        "phase": "第10阶段：高级算法",
        "steps": [
            {
                "concept": "贪心算法：每一步都选择当前最优的策略，最终得到全局最优解。\n\n适用条件：\n1. 最优子结构 - 局部最优能推导出全局最优\n2. 无后效性 - 当前选择不影响后续选择\n\n经典问题：\n• 活动选择（区间调度）\n• 找零钱问题（特定面值下）\n• 最小生成树（Kruskal/Prim）\n• 哈夫曼编码\n• 最短路径（Dijkstra就是贪心）\n\n活动选择模板：\n  按结束时间排序，每次选结束最早的。\n  sort(activities.begin(), activities.end(), \n       [](auto& a, auto& b) { return a.second < b.second; });",
                "example": "#include <iostream>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\n// 活动选择问题\n// 每个活动有开始时间和结束时间，选择最多的活动\nint max_activities(vector<pair<int,int>>& acts) {\n    // 按结束时间排序\n    sort(acts.begin(), acts.end(),\n         [](auto& a, auto& b) { return a.second < b.second; });\n    \n    int count = 1;\n    int last_end = acts[0].second;\n    \n    for (int i = 1; i < acts.size(); i++) {\n        if (acts[i].first >= last_end) {\n            count++;\n            last_end = acts[i].second;\n        }\n    }\n    return count;\n}\n\nint main() {\n    vector<pair<int,int>> activities = {\n        {1, 4}, {3, 5}, {0, 6}, {5, 7}, \n        {3, 8}, {5, 9}, {6, 10}, {8, 11}\n    };\n    \n    cout << \"最多可选 \" << max_activities(activities) << \" 个活动\" << endl;\n    \n    // 找零钱问题（贪心）\n    vector<int> coins = {25, 10, 5, 1};  // 美分\n    int amount = 67;\n    cout << amount << \" 美分 =\";\n    for (int c : coins) {\n        int cnt = amount / c;\n        if (cnt > 0) {\n            cout << \" \" << cnt << \"×\" << c;\n            amount -= cnt * c;\n        }\n    }\n    cout << endl;\n    \n    return 0;\n}",
                "exercise": {
                    "description": "活动选择问题：输入 n 个活动的开始和结束时间，最多能参加多少个活动？\n\n输入：\n4\n1 3\n2 5\n3 7\n4 6\n输出：2\n\n提示：按结束时间排序，贪心选择",
                    "template": "#include <iostream>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    int n;\n    cin >> n;\n    vector<pair<int,int>> acts(n);\n    for (int i = 0; i < n; i++) {\n        cin >> acts[i].first >> acts[i].second;\n    }\n    \n    \n    \n    return 0;\n}",
                    "sample_input": "4\n1 3\n2 5\n3 7\n4 6",
                    "sample_output": "2"
                }
            }
        ]
    },
    {
        "id": 35,
        "name": "二分答案 - 猜答案技术",
        "phase": "第10阶段：高级算法",
        "steps": [
            {
                "concept": "二分答案（Binary Search on Answer）：当答案有单调性时，直接二分答案，然后验证。\n\n模板：\n  int left = min_possible, right = max_possible;\n  while (left < right) {\n      int mid = left + (right - left) / 2;\n      if (check(mid)) {\n          right = mid;  // 或 left = mid + 1\n      } else {\n          left = mid + 1;  // 或 right = mid\n      }\n  }\n\n经典问题：\n• 砍树问题（P1873）\n• 跳石头（P2678）\n• 进击的奶牛（P1824）\n• 木材加工\n\n验证函数（check）是核心，复杂度通常 O(n) 或 O(n log n)。",
                "example": "#include <iostream>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\n// 砍树问题：给定树的高度和需要的木材总量\n// 求锯子的最大高度\nbool can_cut(const vector<int>& trees, int height, int need) {\n    long long total = 0;\n    for (int h : trees) {\n        if (h > height)\n            total += h - height;\n    }\n    return total >= need;\n}\n\nint main() {\n    vector<int> trees = {20, 15, 10, 17};\n    int need = 7;\n    \n    int left = 0, right = *max_element(trees.begin(), trees.end());\n    int result = 0;\n    \n    while (left <= right) {\n        int mid = left + (right - left) / 2;\n        if (can_cut(trees, mid, need)) {\n            result = mid;      // 可行，试试更高的\n            left = mid + 1;\n        } else {\n            right = mid - 1;   // 不行，降低高度\n        }\n    }\n    \n    cout << \"最大高度: \" << result << endl;  // 15\n    \n    // 检验\n    long long total = 0;\n    for (int h : trees) if (h > result) total += h - result;\n    cout << \"能获得木材: \" << total << endl;  // 7\n    \n    return 0;\n}",
                "exercise": {
                    "description": "二分答案 - 木材加工问题。\n有 n 根原木，需要切成 k 段长度相等的小段，求小段的最大长度。\n\n输入：\n3 7\n10 15 20\n输出：5\n\n解释：10→2段5，15→3段5，20→4段5，共9段≥7段\n\n二分范围：0 到 max(woods)",
                    "template": "#include <iostream>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nbool can_cut(const vector<int>& woods, int len, int k) {\n    long long count = 0;\n    for (int w : woods) count += w / len;\n    return count >= k;\n}\n\nint main() {\n    int n, k;\n    cin >> n >> k;\n    vector<int> woods(n);\n    for (int i = 0; i < n; i++) cin >> woods[i];\n    \n    int left = 1, right = *max_element(woods.begin(), woods.end());\n    int ans = 0;\n    \n    \n    \n    return 0;\n}",
                    "sample_input": "3 7\n10 15 20",
                    "sample_output": "5"
                }
            }
        ]
    },

    # ============================================================
    # 第11阶段：并发与多线程
    # ============================================================
    {
        "id": 36,
        "name": "多线程基础 - thread",
        "phase": "第11阶段：并发与多线程",
        "steps": [
            {
                "concept": "C++11 引入了标准线程库。\n需要 #include <thread>\n\n  #include <thread>\n  \n  void worker(int id) {\n      cout << \"线程 \" << id << \" 启动\" << endl;\n  }\n  \n  int main() {\n      thread t1(worker, 1);\n      thread t2(worker, 2);\n      \n      t1.join();  // 等待t1结束\n      t2.join();  // 等待t2结束\n      \n      return 0;\n  }\n\nmutex（互斥锁）：保护共享数据\n  #include <mutex>\n  mutex mtx;\n  mtx.lock();\n  // 访问共享数据\n  mtx.unlock();\n  \n  // 推荐用 lock_guard 自动管理\n  {\n      lock_guard<mutex> lock(mtx);\n      // 自动加锁，离开作用域自动解锁\n  }",
                "example": "#include <iostream>\n#include <thread>\n#include <mutex>\n#include <vector>\nusing namespace std;\n\nmutex mtx;\nint counter = 0;\n\nvoid increment(int times) {\n    for (int i = 0; i < times; i++) {\n        lock_guard<mutex> lock(mtx);\n        counter++;\n    }\n    cout << \"线程 \" << this_thread::get_id() << \" 完成\" << endl;\n}\n\nint main() {\n    vector<thread> threads;\n    \n    // 启动4个线程\n    for (int i = 0; i < 4; i++) {\n        threads.emplace_back(increment, 100000);\n    }\n    \n    // 等待所有线程完成\n    for (auto& t : threads) {\n        t.join();\n    }\n    \n    cout << \"最终结果: \" << counter << endl;\n    cout << \"预期结果: \" << 4 * 100000 << endl;\n    \n    return 0;\n}",
                "exercise": {
                    "description": "创建两个线程，分别计算 1-500000 和 500001-1000000 的和，最后输出总和。\n\n（此练习在本地编译器中运行）\n\n输出：500000500000",
                    "template": "#include <iostream>\n#include <thread>\nusing namespace std;\n\nlong long sum1 = 0, sum2 = 0;\n\nvoid calc(int start, int end, long long& result) {\n    \n}\n\nint main() {\n    thread t1(calc, 1, 500000, ref(sum1));\n    thread t2(calc, 500001, 1000000, ref(sum2));\n    \n    t1.join();\n    t2.join();\n    \n    cout << sum1 + sum2 << endl;\n    return 0;\n}",
                    "sample_input": "",
                    "sample_output": "500000500000"
                }
            }
        ]
    },

    # ============================================================
    # 第12阶段：设计模式与工程实践
    # ============================================================
    {
        "id": 37,
        "name": "单例模式与工厂模式",
        "phase": "第12阶段：设计模式与工程实践",
        "steps": [
            {
                "concept": "设计模式是解决常见问题的成熟方案。\n\n单例模式（Singleton）：全局只有一个实例。\n  class Singleton {\n  private:\n      static Singleton* instance;\n      Singleton() {}\n  public:\n      static Singleton* getInstance() {\n          if (!instance)\n              instance = new Singleton();\n          return instance;\n      }\n  };\n\n工厂模式（Factory）：创建对象而不暴露创建逻辑。\n  class Product {\n  public:\n      virtual void use() = 0;\n  };\n  \n  class ConcreteProductA : public Product {\n      void use() override { cout << \"Product A\"; }\n  };\n  \n  class Factory {\n  public:\n      static Product* create(string type) {\n          if (type == \"A\") return new ConcreteProductA();\n          return nullptr;\n      }\n  };",
                "example": "#include <iostream>\n#include <memory>\n#include <map>\nusing namespace std;\n\n// 单例 - 日志系统\nclass Logger {\nprivate:\n    static Logger* instance;\n    Logger() {}\npublic:\n    static Logger* getInstance() {\n        if (!instance) {\n            instance = new Logger();\n            cout << \"Logger 初始化\" << endl;\n        }\n        return instance;\n    }\n    \n    void log(const string& msg) {\n        cout << \"[LOG] \" << msg << endl;\n    }\n};\nLogger* Logger::instance = nullptr;\n\n// 工厂 - 图形创建\nclass Shape {\npublic:\n    virtual void draw() = 0;\n    virtual ~Shape() {}\n};\n\nclass Circle : public Shape {\npublic:\n    void draw() override { cout << \"画圆形\" << endl; }\n};\n\nclass Square : public Shape {\npublic:\n    void draw() override { cout << \"画正方形\" << endl; }\n};\n\nclass ShapeFactory {\npublic:\n    static unique_ptr<Shape> create(const string& type) {\n        if (type == \"circle\") return make_unique<Circle>();\n        if (type == \"square\") return make_unique<Square>();\n        return nullptr;\n    }\n};\n\nint main() {\n    // 单例测试\n    Logger* log1 = Logger::getInstance();\n    Logger* log2 = Logger::getInstance();\n    cout << \"log1 == log2? \" << (log1 == log2) << endl;  // 1\n    log1->log(\"程序启动\");\n    \n    // 工厂测试\n    auto shape1 = ShapeFactory::create(\"circle\");\n    auto shape2 = ShapeFactory::create(\"square\");\n    shape1->draw();\n    shape2->draw();\n    \n    return 0;\n}",
                "exercise": {
                    "description": "实现一个简单的单例类 Config，存储配置信息。\n提供 getInstance() 和 get/set 方法。\n\n输入：两个字符串 key 和 value\n输出：\"配置已保存: key=value\"",
                    "template": "#include <iostream>\n#include <string>\n#include <map>\nusing namespace std;\n\nclass Config {\nprivate:\n    static Config* instance;\n    map<string, string> data;\n    Config() {}\npublic:\n    \n    void set(const string& key, const string& value) {\n        data[key] = value;\n    }\n    string get(const string& key) {\n        return data.count(key) ? data[key] : \"\";\n    }\n};\n\nConfig* Config::instance = nullptr;\n\nint main() {\n    string key, value;\n    cin >> key >> value;\n    Config* cfg = Config::getInstance();\n    cfg->set(key, value);\n    cout << \"配置已保存: \" << key << \"=\" << cfg->get(key) << endl;\n    return 0;\n}",
                    "sample_input": "language C++",
                    "sample_output": "配置已保存: language=C++"
                }
            }
        ]
    },

    # ============================================================
    # 第13阶段：大型综合项目
    # ============================================================
    {
        "id": 38,
        "name": "项目实战 - 通讯录系统",
        "phase": "第13阶段：大型综合项目",
        "steps": [
            {
                "concept": "开发一个完整的通讯录管理系统，综合运用所学知识。\n\n功能：\n1. 添加联系人（姓名、电话、邮箱）\n2. 显示所有联系人\n3. 按姓名查找\n4. 删除联系人\n5. 按姓名排序\n6. 保存到文件\n\n涉及的知识点：\n• class 和 vector\n• string 操作\n• 文件 I/O\n• 排序和查找\n• 命令行菜单",
                "example": "#include <iostream>\n#include <vector>\n#include <string>\n#include <fstream>\n#include <algorithm>\nusing namespace std;\n\nclass Contact {\npublic:\n    string name;\n    string phone;\n    string email;\n    \n    Contact(const string& n, const string& p, const string& e = \"\")\n        : name(n), phone(p), email(e) {}\n    \n    void display() const {\n        cout << name << \" | \" << phone;\n        if (!email.empty()) cout << \" | \" << email;\n        cout << endl;\n    }\n};\n\nclass AddressBook {\nprivate:\n    vector<Contact> contacts;\n    string filename;\n    \npublic:\n    AddressBook(const string& fn) : filename(fn) {\n        load();\n    }\n    \n    void add(const string& name, const string& phone, const string& email = \"\") {\n        contacts.push_back(Contact(name, phone, email));\n        save();\n        cout << \"✅ 已添加: \" << name << endl;\n    }\n    \n    void show_all() const {\n        if (contacts.empty()) {\n            cout << \"📭 通讯录为空\" << endl;\n            return;\n        }\n        cout << \"\\n📋 通讯录 (共\" << contacts.size() << \"人):\" << endl;\n        for (const auto& c : contacts) {\n            cout << \"  \";\n            c.display();\n        }\n    }\n    \n    void search(const string& keyword) const {\n        bool found = false;\n        for (const auto& c : contacts) {\n            if (c.name.find(keyword) != string::npos) {\n                c.display();\n                found = true;\n            }\n        }\n        if (!found) cout << \"未找到: \" << keyword << endl;\n    }\n    \n    void sort_by_name() {\n        sort(contacts.begin(), contacts.end(),\n             [](const Contact& a, const Contact& b) {\n                 return a.name < b.name;\n             });\n        save();\n        cout << \"✅ 已按姓名排序\" << endl;\n    }\n    \n    void save() const {\n        ofstream fout(filename);\n        for (const auto& c : contacts) {\n            fout << c.name << \",\" << c.phone << \",\" << c.email << endl;\n        }\n    }\n    \n    void load() {\n        contacts.clear();\n        ifstream fin(filename);\n        if (!fin) return;\n        string line;\n        while (getline(fin, line)) {\n            // 简单解析\n            auto pos1 = line.find(',');\n            auto pos2 = line.rfind(',');\n            if (pos1 != string::npos) {\n                string n = line.substr(0, pos1);\n                string p = line.substr(pos1 + 1, pos2 - pos1 - 1);\n                string e = line.substr(pos2 + 1);\n                contacts.push_back(Contact(n, p, e));\n            }\n        }\n    }\n};\n\nint main() {\n    AddressBook book(\"contacts.txt\");\n    \n    book.add(\"张三\", \"13800138000\", \"zhangsan@email.com\");\n    book.add(\"李四\", \"13900139000\");\n    book.add(\"王五\", \"13700137000\", \"wangwu@email.com\");\n    \n    book.show_all();\n    \n    cout << \"\\n搜索 '张':\" << endl;\n    book.search(\"张\");\n    \n    book.sort_by_name();\n    book.show_all();\n    \n    return 0;\n}",
                "exercise": {
                    "description": "在本地编译器中实现通讯录管理系统。\n本题为项目实战，请参考示例代码实现。\n\n此处直接输出\"通讯录系统创建成功\"即可。",
                    "template": "#include <iostream>\nusing namespace std;\n\nint main() {\n    cout << \"通讯录系统创建成功\" << endl;\n    cout << \"请在本地编译器中运行完整实现\" << endl;\n    return 0;\n}",
                    "sample_input": "",
                    "sample_output": "通讯录系统创建成功\n请在本地编译器中运行完整实现"
                }
            }
        ]
    },
    {
        "id": 39,
        "name": "项目实战 - 控制台小游戏",
        "phase": "第13阶段：大型综合项目",
        "steps": [
            {
                "concept": "用C++开发一个猜数字控制台游戏。\n\n功能：\n1. 计算机随机生成1-100的数字\n2. 玩家猜数字\n3. 提示\"大了\"或\"小了\"\n4. 记录猜的次数\n5. 用不同的颜色显示\n\n涉及知识点：\n• random\n• 循环和条件\n• 函数\n• 输入验证\n• 游戏状态管理",
                "example": "#include <iostream>\n#include <random>\n#include <ctime>\nusing namespace std;\n\nclass GuessGame {\nprivate:\n    int target;\n    int attempts;\n    int max_range;\n    \npublic:\n    GuessGame(int max_r = 100) : max_range(max_r), attempts(0) {\n        srand(time(nullptr));\n    }\n    \n    void new_game() {\n        target = rand() % max_range + 1;\n        attempts = 0;\n        cout << \"\\n🎮 猜数字游戏!\" << endl;\n        cout << \"范围: 1-\" << max_range << endl;\n    }\n    \n    bool guess(int num) {\n        attempts++;\n        if (num == target) {\n            cout << \"🎉 恭喜！猜对了！\" << endl;\n            cout << \"用了 \" << attempts << \" 次\" << endl;\n            return true;\n        } else if (num < target) {\n            cout << \"📈 小了\" << endl;\n        } else {\n            cout << \"📉 大了\" << endl;\n        }\n        return false;\n    }\n    \n    int get_attempts() const { return attempts; }\n};\n\nint main() {\n    GuessGame game;\n    game.new_game();\n    \n    int guess_num;\n    while (true) {\n        cout << \"请输入你的猜测: \";\n        cin >> guess_num;\n        if (game.guess(guess_num)) {\n            break;\n        }\n    }\n    \n    return 0;\n}",
                "exercise": {
                    "description": "猜数字游戏项目。\n在本地编译器中实现并运行。\n\n此处直接输出\"猜数字游戏创建成功\"。",
                    "template": "#include <iostream>\nusing namespace std;\n\nint main() {\n    cout << \"猜数字游戏创建成功\" << endl;\n    cout << \"请在本地编译器中运行\" << endl;\n    return 0;\n}",
                    "sample_input": "",
                    "sample_output": "猜数字游戏创建成功\n请在本地编译器中运行"
                }
            }
        ]
    }
]

PHASES_CPP_V3 = [
    "第8阶段：高级STL与实用技巧",
    "第9阶段：图论与数据结构",
    "第10阶段：高级算法",
    "第11阶段：并发与多线程",
    "第12阶段：设计模式与工程实践",
    "第13阶段：大型综合项目"
]
