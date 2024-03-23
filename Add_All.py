def divide_and_conquer(start, end):
    if start >= end:
        return 0

    mid = (start + end) // 2
    left_sum = divide_and_conquer(start, mid)
    right_sum = divide_and_conquer(mid + 1, end)

    partial_sum = 0
    left_value = 0
    right_value = 0

    for i in range(mid, start - 1, -1):
        left_value += nums[i]
        partial_sum = max(partial_sum, left_value)

    for i in range(mid + 1, end):
        right_value += nums[i]
        partial_sum = max(partial_sum, right_value)

    return max(left_sum, right_sum, partial_sum)

while True:
    try:
        n = int(input())
        nums = list(map(int, input().split()))
        print(divide_and_conquer(0, n))
    except:
        break
