import sys

def carry_op(a, b):
    result = []
    carry = 0
    a = a[::-1]
    b = b[::-1]
    for i in range(max(len(a), len(b))):
        x = int(a[i]) if i < len(a) else 0
        y = int(b[i]) if i < len(b) else 0
        s = x + y + carry
        result.append(str(s % 10))
        carry = s // 10
    if carry:
        result.append(str(carry))
    return ''.join(reversed(result))

cases = int(sys.stdin.readline())
for _ in range(cases):
    a, b = sys.stdin.readline().split()
    print(carry_op(a, b))
