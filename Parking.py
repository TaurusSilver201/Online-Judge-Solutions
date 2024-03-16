cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    min_cost = float('inf')
    for i in range(n):
        cost = 0
        for j in range(n):
            cost += abs(arr[j] - (i+1))
        min_cost = min(min_cost, cost)
    print(min_cost)
