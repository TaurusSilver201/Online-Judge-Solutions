import sys
from collections import deque

while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    dist = [float('inf')] * n
    dist[0] = 0
    queue = deque([(0, 0)])
    while queue:
        u, d = queue.popleft()
        for v, w in graph[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                queue.append((v, dist[v]))
    for i in range(1, n):
        if dist[i] == float('inf'):
            print('No Path')
        else:
            print(dist[i])
