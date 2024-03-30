from collections import defaultdict

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

cases = int(input())
for _ in range(cases):
    n, m = map(int, input().split())
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        union_sets(parent, rank, a, b)
    clubs = defaultdict(list)
    for i in range(1, n + 1):
        root = find_set(parent, i)
        clubs[root].append(i)
    print(len(clubs))
    for members in clubs.values():
        print(*sorted(members))
