#include <assert.h>
#include <stdlib.h>

int uniquePaths(int m, int n) {
    int* paths = (int *)malloc(sizeof(int) * (m*n));
    int i = 0;
    for(i = 0; i < n; i++)
        paths[i] = 1;
    for(i = 0; i < m; i++) 
        paths[i*n] = 1;
    int j = 1;
    for(i = 1; i < m; i++) 
        for(j = 1; j < n; j++)
            paths[i*n+j] = paths[(i-1)*n+j] + paths[i*n+j-1];
    return paths[m*n-1];
}

int main() {
    assert(uniquePaths(3, 3) == 6);

    return 0;
}
