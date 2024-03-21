import sys
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

while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
    
    parent = list(range(n))
    rank = [0] * n
    edges = []
    total_cost = 0
    for _ in range(m):
        x, y, z = map(int, sys.stdin.readline().split())
        edges.append((x, y, z))
        total_cost += z
    
    edges.sort(key=lambda x: x[2])
    min_cost = 0
    for u, v, w in edges:
        if find_set(parent, u) != find_set(parent, v):
            min_cost += w
            union_sets(parent, rank, u, v)
    
    print(total_cost - min_cost)
