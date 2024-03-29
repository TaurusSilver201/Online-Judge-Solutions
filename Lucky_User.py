from collections import defaultdict

def solve(n, k, users):
    lucky_users = defaultdict(int)
    for user in users:
        lucky_users[user] += 1
    lucky_users = sorted(lucky_users.items(), key=lambda x: (-x[1], x[0]))
    result = []
    for user, count in lucky_users[:k]:
        result.append((user, count))
    return result

cases = int(input())
for _ in range(cases):
    n, k = map(int, input().split())
    users = list(map(int, input().split()))
    result = solve(n, k, users)
    print(f"Case #{_ + 1}:")
    for user, count in result:
        print(f"{user} {count}")
