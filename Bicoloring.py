from collections import deque

def bipartite(graph):
    n = len(graph)
    colors = [-1] * n
    for start in range(n):
        if colors[start] == -1:
            queue = deque([(start, 0)])
            colors[start] = 0
            while queue:
                u, color = queue.popleft()
                for v in graph[u]:
                    if colors[v] == -1:
                        colors[v] = 1 - color
                        queue.append((v, 1 - color))
                    elif colors[v] == color:
                        return False
    return True

cases = int(input())
for _ in range(cases):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    if bipartite(graph):
        print('BICOLORABLE.')
    else:
        print('NOT BICOLORABLE.')
