import math

cases = int(input())
for _ in range(cases):
    n = int(input())
    coords = []
    for _ in range(n):
        x, y = map(int, input().split())
        coords.append((x, y))
    min_cost = float('inf')
    for x1, y1 in coords:
        cost = 0
        for x2, y2 in coords:
            if x1 != x2 or y1 != y2:
                cost += math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        min_cost = min(min_cost, cost)
    print(f'{min_cost:.2f}')
