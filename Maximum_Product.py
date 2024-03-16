from collections import deque

while True:
    n = int(input())
    if n == 0:
        break
    arr = deque(map(int, input().split()))
    max_prod = 0
    for i in range(n):
        prod = arr.popleft()
        for j in range(i+1, n):
            prod = (prod * arr.popleft()) % 1000
            max_prod = max(max_prod, prod)
    print(max_prod)
