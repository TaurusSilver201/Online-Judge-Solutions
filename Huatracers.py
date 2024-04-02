from collections import deque

def bfs(grid, start):
    n, m = len(grid), len(grid[0])
    queue = deque([(start, 0)])
    visited = [[False] * m for _ in range(n)]
    visited[start[0]][start[1]] = True

    while queue:
        (x, y), cost = queue.popleft()

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] != '#':
                if grid[nx][ny] == 'H':
                    return cost + 1
                visited[nx][ny] = True
                queue.append(((nx, ny), cost + 1))

    return -1

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    grid = []
    start = None

    for i in range(n):
        row = list(input())
        for j in range(m):
            if row[j] == 'S':
                start = (i, j)
        grid.append(row)

    min_cost = bfs(grid, start)
    if min_cost == -1:
        print("No solution")
    else:
        print(min_cost)
