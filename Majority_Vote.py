from collections import Counter

cases = int(input())
for _ in range(cases):
    n = int(input())
    students = []
    for _ in range(n):
        students.append(input().split())

    max_count = 0
    majority_subjects = []
    for i in range(1, 21):
        subject_count = sum(str(i) in student for student in students)
        if subject_count > n // 2 and subject_count > max_count:
            max_count = subject_count
            majority_subjects = [i]
        elif subject_count == max_count:
            majority_subjects.append(i)

    print(*sorted(majority_subjects))
