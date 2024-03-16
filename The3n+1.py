def cycle_length(n):
    count = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count

cases = int(input())
for _ in range(cases):
    i, j = map(int, input().split())
    i, j = min(i, j), max(i, j)
    max_cycle = 0
    for n in range(i, j+1):
        cycle = cycle_length(n)
        max_cycle = max(max_cycle, cycle)
    print(i, j, max_cycle)
