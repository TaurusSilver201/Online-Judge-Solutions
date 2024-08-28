def find_root(parent, i):
    if parent[i] == -1:
        return i
    parent[i] = find_root(parent, parent[i])
    return parent[i]

def union(parent, size, a, b):
    root_a = find_root(parent, a)
    root_b = find_root(parent, b)

    if root_a == root_b:
        return

    if size[root_a] < size[root_b]:
        parent[root_a] = root_b
        size[root_b] += size[root_a]
    else:
        parent[root_b] = root_a
        size[root_a] += size[root_b]


while True:
    try:
        n, m = map(int, input().split())
    except:
        break

    parent = [-1] * (n + 1)
    size = [1] * (n + 1)

    for _ in range(m):
        p = int(input())
        ancestors = list(map(int, input().split()))

        for bee in ancestors:
            union(parent, size, p, bee)

    max_size = max(size)
    print(max_size)
