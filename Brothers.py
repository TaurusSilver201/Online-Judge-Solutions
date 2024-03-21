import sys
from collections import deque

def bfs(start, end, graph):
    queue = deque([(start, 0)])
    visited = [False] * len(graph)
    visited[start] = True
    while queue:
        node, cost = queue.popleft()
        if node == end:
            return cost
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, cost+1))
    return -1

cases = int(sys.stdin.readline())
for _ in range(cases):
    n, m, x, y = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    min_cost = bfs(x, y, graph)
    print(min_cost)
