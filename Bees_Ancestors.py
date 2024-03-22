#include <stdio.h>
#include <string.h>

int main() {
    int n, m, p;
    int parent[100001];
    int size[100001];
    memset(parent, -1, sizeof(parent));
    memset(size, 0, sizeof(size));

    while (scanf("%d %d", &n, &m) != EOF) {
        for (int i = 1; i <= n; i++) {
            parent[i] = -1;
            size[i] = 1;
        }

        for (int i = 0; i < m; i++) {
            scanf("%d", &p);
            int root = p;
            while (parent[root] != -1) {
                root = parent[root];
            }

            for (int j = 0; j < p - 1; j++) {
                scanf("%d", &p);
                int p_root = p;
                while (parent[p_root] != -1) {
                    p_root = parent[p_root];
                }

                if (p_root != root) {
                    if (size[p_root] > size[root]) {
                        parent[root] = p_root;
                        size[p_root] += size[root];
                    } else {
                        parent[p_root] = root;
                        size[root] += size[p_root];
                    }
                }
            }
        }

        int max_size = 0;
        for (int i = 1; i <= n; i++) {
            if (parent[i] == -1) {
                max_size = size[i] > max_size ? size[i] : max_size;
            }
        }

        printf("%d\n", max_size);
    }

    return 0;
}
