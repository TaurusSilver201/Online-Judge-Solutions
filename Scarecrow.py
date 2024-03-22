def max_distance(points):
    points.sort(key=lambda x: x[0])  # Sort by x-coordinate
    max_diff_x = max(points[i][0] - points[i - 1][0] for i in range(1, len(points)))

    points.sort(key=lambda x: x[1])  # Sort by y-coordinate
    max_diff_y = max(points[i][1] - points[i - 1][1] for i in range(1, len(points)))

    return max_diff_x * max_diff_y

cases = int(input())
for _ in range(cases):
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    print(max_distance(points))
