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

cases = 1
while True:
    n = int(input())
    if n == 0:
        break

    graph = defaultdict(list)
    for _ in range(n):
        line = input().split()
        for i in range(1, len(line)):
            graph[line[i]].append(line[0])

    sorted_order = topological_sort(graph)
    if sorted_order:
        print(f"Case #{cases}: {' '.join(sorted_order)}")
    else:
        print(f"Case #{cases}: No valid order exists")
    cases += 1
