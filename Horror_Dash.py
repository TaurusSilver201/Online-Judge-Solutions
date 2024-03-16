cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    max_speed = max(arr)
    curr_speed = 0
    time = 0
    for speed in arr:
        time += max_speed - curr_speed
        curr_speed = speed
    time += max_speed
    print(time)
