from collections import deque

def bfs(grid, start, end):
    n, m = len(grid), len(grid[0])
    queue = deque([(start, 0)])
    visited = [[False] * m for _ in range(n)]
    visited[start[0]][start[1]] = True

    while queue:
        (x, y), cost = queue.popleft()
        if (x, y) == end:
            return cost

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] != 'X':
                visited[nx][ny] = True
                new_cost = cost + 1 if grid[nx][ny] != grid[x][y] else cost
                queue.append(((nx, ny), new_cost))

    return -1

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    grid = []
    start = None
    end = None

    for i in range(n):
        row = list(input())
        for j in range(m):
            if row[j] == 'S':
                start = (i, j)
            elif row[j] == 'T':
                end = (i, j)
        grid.append(row)

    min_cost = bfs(grid, start, end)
    if min_cost == -1:
        print("Not possible")
    else:
        print(f"Minimum number of steps = {min_cost}")
