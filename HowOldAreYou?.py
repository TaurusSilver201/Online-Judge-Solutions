def age(day, month, year):
    return (year - 1, 12 - month, 31 - day)

def solve(births, queries):
    ages = []
    for q in queries:
        q_day, q_month, q_year = q
        max_age = (-1, -1, -1)
        for b in births:
            b_day, b_month, b_year = b
            if q_year < b_year:
                continue
            elif q_year == b_year:
                if q_month < b_month:
                    continue
                elif q_month == b_month:
                    if q_day < b_day:
                        continue
            age_years, age_months, age_days = age(b_day, b_month, b_year)
            max_age = max(max_age, (age_years, age_months, age_days))
        ages.append(max_age)
    return ages

n = int(input())
births = []
for _ in range(n):
    day, month, year = map(int, input().split())
    births.append((day, month, year))

q = int(input())
queries = []
for _ in range(q):
    day, month, year = map(int, input().split())
    queries.append((day, month, year))

ages = solve(births, queries)
for age in ages:
    years, months, days = age
    print(f"{years} years, {months} months, {days} days")
