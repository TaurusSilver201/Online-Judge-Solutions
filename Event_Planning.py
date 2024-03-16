from collections import defaultdict

while True:
    try:
        n, b, h, w = map(int, input().split())
    except:
        break
    price = defaultdict(int)
    for _ in range(h):
        p, m = map(int, input().split())
        price[p] += m
    min_cost = float('inf')
    for p in sorted(price.keys()):
        curr_cost = 0
        beds = 0
        for hotel_p, hotel_beds in sorted(price.items()):
            if beds + hotel_beds > n:
                curr_cost += (n - beds) * min(p, hotel_p)
                break
            curr_cost += hotel_beds * hotel_p
            beds += hotel_beds
        min_cost = min(min_cost, curr_cost * n)
    print(min_cost)
