from collections import deque

def bfs(start, end, graph):
    queue = deque([(start, [])])
    visited = set()
    while queue:
        node, path = queue.popleft()
        if node == end:
            return path
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    return []

while True:
    try:
        n, m = map(int, input().split())
    except:
        break
    graph = {}
    for _ in range(n):
        line = input().split()
        node = int(line[0])
        neighbors = list(map(int, line[2:]))
        graph[node] = neighbors
    start, end = map(int, input().split())
    path = bfs(start, end, graph)
    if not path:
        print(f'Impossible')
    else:
        print(f'{len(path)} {" ".join(map(str, path))}')
