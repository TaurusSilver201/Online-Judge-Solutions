import sys

def radix_sort(strings, max_len):
    for digit in range(max_len - 1, -1, -1):
        buckets = [[] for _ in range(27)]
        for string in strings:
            index = ord(string[digit]) - ord('A') if digit < len(string) else 0
            buckets[index].append(string)
        strings = []
        for bucket in buckets:
            strings.extend(bucket)
    return strings

cases = int(sys.stdin.readline())
for _ in range(cases):
    n, m = map(int, sys.stdin.readline().split())
    dna = [sys.stdin.readline().strip() for _ in range(n)]
    max_len = max(len(s) for s in dna)
    sorted_dna = radix_sort(dna, max_len)
    for sequence in sorted_dna:
        print(sequence)
    if _ < cases - 1:
        print()
