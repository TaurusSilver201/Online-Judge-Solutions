cases = int(input())
for _ in range(cases):
    a, b, c = map(int, input().split())
    if a > b:
        op = '>'
    elif a < b:
        op = '<'
    else:
        op = '='
    if c:
        print('Case', _, ':', op)
    else:
        print('Case', _, ':', op, end='')
