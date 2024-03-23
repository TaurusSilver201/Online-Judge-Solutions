def gray_code(n):
    if n == 0:
        return ['0']
    if n == 1:
        return ['0', '1']

    prev_codes = gray_code(n - 1)
    current_codes = []
    for code in prev_codes:
        current_codes.append('0' + code)
    for code in reversed(prev_codes):
        current_codes.append('1' + code)
    return current_codes

cases = int(input())
for _ in range(cases):
    n = int(input())
    codes = gray_code(n)
    for code in codes:
        print(code)
    print()
