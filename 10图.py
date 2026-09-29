# # ===== 用邻接表表示无向图 =====
# graph = {
#     "你": ["小明", "小红", "小刚"],
#     "小明": ["你", "小丽"],
#     "小红": ["你", "小刚"],
#     "小刚": ["你", "小红"],
#     "小丽": ["小明"]
# }
#
# # ===== 遍历某人的好友 =====
# def get_friends(person):
#     return graph.get(person, [])   # 如果这个人不在图里，返回空列表
#
# print(get_friends("你"))      # ['小明', '小红', '小刚']
# print(get_friends("小丽"))    # ['小明']
#
# # ===== 判断两个人是否直接相连 =====
# def are_connected(person1, person2):
#     return person2 in graph.get(person1, [])
#
# print(are_connected("你", "小红"))   # True
# print(are_connected("你", "小丽"))   # False
#
# # ===== 统计图里有多少个顶点和边 =====
# vertices = list(graph.keys())
# edges = sum(len(neighbors) for neighbors in graph.values()) // 2  # 无向图每条边被算2次
# print(len(vertices))   # 5
# print(edges)           # 5（你-小明，你-小红，你-小刚，小明-小丽，小刚-小红）


from collections import deque

def has_path_bfs(n, edges, start, end):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * n           # 修复硬编码
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        if node == end:
            return True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return False

print("BFS：",has_path_bfs(3, [[0,1],[1,2]], start = 0, end = 2))


def has_path_dfs(n, edges, start, end):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * n           # 修复硬编码

    def dfs(node):
        if node == end:
            return True
        visited[node] = True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                if dfs(neighbor):
                    return True

        return False

    return dfs(start)

print("DFS：",has_path_dfs(3, [[0,1],[1,2]], start = 0, end = 2))


