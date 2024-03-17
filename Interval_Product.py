import sys

def multiply(a, b):
    sign = (a[0] * b[0]) // abs(a[0] * b[0])
    value = abs(a[1] * b[1])
    mod = abs(a[2] * b[2])
    return (sign, value, mod)

def power(a, n):
    if n == 0:
        return (1, 1, 1)
    elif n % 2 == 0:
        temp = power(a, n // 2)
        return multiply(temp, temp)
    else:
        temp = power(a, n // 2)
        return multiply(multiply(temp, temp), a)

while True:
    try:
        n, k, m = map(int, sys.stdin.readline().split())
    except:
        break
    a = (1, n, m)
    result = power(a, k)
    print(result[1])
