import sys

for line in sys.stdin:
    n, m = map(int, line.split())
    while n != 0 and m != 0:
        print(n // m, n % m)
        n, m = map(int, sys.stdin.readline().split())
