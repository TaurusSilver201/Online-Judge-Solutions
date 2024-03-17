def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

while True:
    try:
        n = int(input())
    except:
        break
    nums = list(map(int, input().split()))
    lcm_val = nums[0]
    for num in nums[1:]:
        lcm_val = lcm(lcm_val, num)
    count = 0
    for i in range(1, lcm_val + 1):
        if lcm_val % i == 0:
            count += 1
    print(count)
