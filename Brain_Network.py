from collections import defaultdict

def dfs(u, visited, graph, order):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v, visited, graph, order)
    order.append(u)

def topological_sort(graph):
    n = len(graph)
    visited = [False] * n
    order = []
    for u in range(n):
        if not visited[u]:
            dfs(u, visited, graph, order)
    order.reverse()
    return order

cases = 1
while True:
    n, m, p = map(int, input().split())
    if n == 0 and m == 0 and p == 0:
        break
    graph = defaultdict(list)
    for _ in range(p):
        a, b = map(int, input().split())
        graph[a].append(b)
    order = topological_sort(graph)
    print(f"Case #{cases}: {' '.join(map(str, order))}")
    cases += 1
