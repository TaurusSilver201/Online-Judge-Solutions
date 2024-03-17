import sys
from collections import deque

def bfs(start, end, graph, n):
    queue = deque([(start, 0)])
    visited = [False] * n
    visited[start] = True
    while queue:
        node, cost = queue.popleft()
        if node == end:
            return cost
        for neighbor, weight in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, cost + weight))
    return -1

cases = int(sys.stdin.readline())
for _ in range(cases):
    n, m, a, b = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        x, y, z = map(int, sys.stdin.readline().split())
        graph[x].append((y, z))
        graph[y].append((x, z))
    print(bfs(a, b, graph, n))
