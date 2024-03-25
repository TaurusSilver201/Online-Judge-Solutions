from collections import defaultdict

def topological_sort(graph):
    in_degree = defaultdict(int)
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    queue = [u for u in graph if in_degree[u] == 0]
    sorted_order = []

    while queue:
        u = queue.pop(0)
        sorted_order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return sorted_order if len(sorted_order) == len(graph) else []

def solve(dependencies):
    graph = defaultdict(list)
    for u, v in dependencies:
        graph[u].append(v)

    sorted_order = topological_sort(graph)
    if not sorted_order:
        return "No"

    return "Yes" if len(sorted_order) == len(graph) else "No"

cases = int(input())
for _ in range(cases):
    n, m = map(int, input().split())
    dependencies = []
    for _ in range(m):
        u, v = map(int, input().split())
        dependencies.append((u, v))
    print(solve(dependencies))
