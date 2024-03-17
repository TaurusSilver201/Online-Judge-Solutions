import sys

def solve(bars):
    bars.sort(reverse=True)
    stack = []
    for bar in bars:
        if not stack or bar < stack[-1]:
            stack.append(bar)
    return len(stack)

cases = int(sys.stdin.readline())
for _ in range(cases):
    n = int(sys.stdin.readline())
    bars = list(map(int, sys.stdin.readline().split()))
    print(solve(bars))
