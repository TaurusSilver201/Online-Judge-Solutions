import sys
from collections import deque

def bfs(start, end, graph, coins):
    queue = deque([(start, 0)])
    visited = [False] * len(graph)
    visited[start] = True
    while queue:
        node, cost = queue.popleft()
        if node == end:
            return cost, coins[node]
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, cost+1))
    return float('inf'), 0

while True:
    try:
        n, m = map(int, sys.stdin.readline().split())
    except:
        break
    
    graph = [[] for _ in range(n)]
    coins = [0] * n
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    
    start, end = map(int, sys.stdin.readline().split())
    for i in map(int, sys.stdin.readline().split()):
        coins[i] = 1
    
    min_cost, max_coins = bfs(start, end, graph, coins)
    print(min_cost, max_coins)
