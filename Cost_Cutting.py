cases = int(input())
for _ in range(cases):
    arr = list(map(int, input().split()))
    n, x, y = arr[0], arr[1], arr[2]
    salaries = arr[3:]
    salaries.sort(reverse=True)
    total_cost = sum(salaries)
    for i in range(x):
        total_cost -= salaries[i]
    for i in range(x, x+y):
        total_cost -= salaries[i] // 3
    print(total_cost)
