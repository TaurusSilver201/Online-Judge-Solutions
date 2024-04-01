from math import factorial

def catalan_number(n):
    return factorial(2 * n) // (factorial(n + 1) * factorial(n))

cases = int(input())
for _ in range(cases):
    n, m = map(int, input().split())
    if n > m:
        n, m = m, n
    if n == 0 or n == m:
        print(1)
    else:
        print(catalan_number(m - n))
