from math import gcd

def solve(a, b, c, d):
    g = gcd(a, b)
    a //= g
    b //= g
    x, y = 0, 0
    while True:
        x += a
        y += b
        if x >= c and y >= d:
            break
    if x >= c and y >= d:
        return x - c, y - d
    return -1, -1

cases = int(input())
for _ in range(cases):
    a, b, c, d = map(int, input().split())
    x, y = solve(a, b, c, d)
    if x == -1 and y == -1:
        print("No solution")
    else:
        print(f"Solution: {x} {y}")
