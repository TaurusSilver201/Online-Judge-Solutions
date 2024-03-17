import sys

def simulate(ants):
    time = 0
    while True:
        # Move ants
        for i in range(len(ants)):
            ants[i] += 1
        time += 1
        # Check for collisions
        for i in range(len(ants)):
            if ants[i] > 0 and ants[i] in ants[:i] + ants[i+1:]:
                return time
        # Check if all ants have fallen
        if all(ant <= 0 for ant in ants):
            return time

cases = int(sys.stdin.readline())
for _ in range(cases):
    n, l = map(int, sys.stdin.readline().split())
    ants = list(map(int, sys.stdin.readline().split()))
    for i in range(n):
        ants[i] = l - ants[i]
    print(simulate(ants))
