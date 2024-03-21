import sys
from collections import deque

def bfs(start, n, m, graph):
    queue = deque([(start, 0)])
    visited = [False] * (n*m)
    visited[start] = True
    while queue:
        node, cost = queue.popleft()
        if node == n*m-1:
            return cost
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, cost+1))
    return -1

cases = 1
while True:
    try:
        n, m, s = map(int, sys.stdin.readline().split())
    except:
        break
    if n == 0 and m == 0 and s == 0:
        break
    
    graph = [[] for _ in range(n*m)]
    for i in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        for j in range(m):
            node = i*m + j
            if row[j] == 0:
                if i > 0:
                    graph[node].append((i-1)*m + j)
                if i < n-1:
                    graph[node].append((i+1)*m + j)
                if j > 0:
                    graph[node].append(i*m + j-1)
                if j < m-1:
                    graph[node].append(i*m + j+1)
    
    start = s-1
    min_cost = bfs(start, n, m, graph)
    print(f'Case {cases}: {min_cost}')
    cases += 1
