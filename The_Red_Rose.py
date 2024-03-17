import sys
from collections import deque

def bfs(grid, start, target):
    n = len(grid)
    m = len(grid[0])
    queue = deque([(start, 0)])
    visited = [[False] * m for _ in range(n)]
    visited[start[0]][start[1]] = True
    while queue:
        (x, y), cost = queue.popleft()
        if (x, y) == target:
            return cost
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] != '#':
                visited[nx][ny] = True
                queue.append(((nx, ny), cost + (1 if grid[nx][ny] == 'x' else 0)))
    return -1

cases = int(sys.stdin.readline())
for _ in range(cases):
    n, m = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().strip()) for _ in range(n)]
    start = None
    target = None
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'P':
                start = (i, j)
            elif grid[i][j] == 'R':
                target = (i, j)
    cost = bfs(grid, start, target)
    print(cost if cost >= 0 else 'Impossible')
