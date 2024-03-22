#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int x, y;
} Point;

int cmp_x(const void *a, const void *b) {
    Point *p1 = (Point *)a, *p2 = (Point *)b;
    return p1->x - p2->x;
}

int cmp_y(const void *a, const void *b) {
    Point *p1 = (Point *)a, *p2 = (Point *)b;
    return p1->y - p2->y;
}

int main() {
    int t, n;
    Point *points;
    scanf("%d", &t);

    while (t--) {
        scanf("%d", &n);
        points = (Point *)malloc(n * sizeof(Point));

        for (int i = 0; i < n; i++) {
            scanf("%d %d", &points[i].x, &points[i].y);
        }

        qsort(points, n, sizeof(Point), cmp_x);
        int max_diff_x = 0;
        for (int i = 1; i < n; i++) {
            max_diff_x = max_diff_x > points[i].x - points[i - 1].x ? max_diff_x : points[i].x - points[i - 1].x;
        }

        qsort(points, n, sizeof(Point), cmp_y);
        int max_diff_y = 0;
        for (int i = 1; i < n; i++) {
            max_diff_y = max_diff_y > points[i].y - points[i - 1].y ? max_diff_y : points[i].y - points[i - 1].y;
        }

        printf("%d\n", max_diff_x * max_diff_y);
        free(points);
    }

    return 0;
}
