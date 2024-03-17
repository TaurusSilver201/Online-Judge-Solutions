import sys

def dfs(x, y):
    if x < 0 or x >= r or y < 0 or y >= c or grid[x][y] != '.' or visited[x][y]:
        return 0
    visited[x][y] = True
    total = 1
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        total += dfs(x+dx, y+dy)
    return total

cases = 1
while True:
    line = sys.stdin.readline().strip()
    if not line:
        break
    r, c = map(int, line.split())
    grid = [list(sys.stdin.readline().strip()) for _ in range(r)]
    visited = [[False] * c for _ in range(r)]
    max_area = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '.' and not visited[i][j]:
                max_area = max(max_area, dfs(i, j))
    print(f'Case {cases}: {max_area}')
    cases += 1
