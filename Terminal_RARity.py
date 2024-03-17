import sys

def build_trie(words):
    trie = {}
    for word in words:
        node = trie
        for char in word:
            node = node.setdefault(char, {})
        node['$'] = word
    return trie

def traverse_trie(trie):
    stack = list(trie.values())
    rare_words = []
    while stack:
        node = stack.pop()
        if '$' in node:
            rare_words.append(node['$'])
        for child in node.values():
            if child not in stack:
                stack.append(child)
    return rare_words

cases = int(sys.stdin.readline())
for _ in range(cases):
    n = int(sys.stdin.readline())
    words = [sys.stdin.readline().strip() for _ in range(n)]
    trie = build_trie(words)
    rare_words = traverse_trie(trie)
    for word in rare_words:
        print(word)
    if _ < cases - 1:
        print()
