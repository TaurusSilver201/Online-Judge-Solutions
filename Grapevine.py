import sys
sys.setrecursionlimit(10 ** 6)

def find_set(parent, i):
    if parent[i] == i:
        return i
    parent[i] = find_set(parent, parent[i])
    return parent[i]

def union_sets(parent, rank, x, y):
    xroot = find_set(parent, x)
    yroot = find_set(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

cases = int(sys.stdin.readline())
for _ in range(cases):
    n, m = map(int, sys.stdin.readline().split())
    parent = list(range(n))
    rank = [0] * n
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        union_sets(parent, rank, a-1, b-1)
    print(sum(1 for i in range(n) if parent[i] == i))
