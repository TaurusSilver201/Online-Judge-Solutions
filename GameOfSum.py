from functools import lru_cache

@lru_cache(maxsize=None)
def game_of_sum(n, k):
    if n == 0:
        return True
    if k == 0:
        return False
    for i in range(1, k+1):
        if not game_of_sum(n-i, i):
            return True
    return False

cases = int(input())
for _ in range(cases):
    n, k = map(int, input().split())
    if game_of_sum(n, k):
        print('Stan wins')
    else:
        print('Ollie wins')
