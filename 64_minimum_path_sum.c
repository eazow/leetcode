#include <assert.h>
#include <stdlib.h>

#define min(A,B) ((A)<(B)?(A):(B))

int minPathSum(int** grid, int gridRowSize, int gridColSize) {
    int i = 0, j = 0;
    for(i = 1; i < gridRowSize; i++)
        grid[i][0] += grid[i-1][0];
    for(j = 1; j < gridColSize; j++) 
        grid[0][j] += grid[0][j-1];

    for(i = 1; i < gridRowSize; i++) {
        for(j = 1; j < gridColSize; j++) {
            grid[i][j] += min(grid[i][j-1], grid[i-1][j]);
        }
    }
    return grid[gridRowSize-1][gridColSize-1];
}

int main() {
    int** grid = (int **)malloc(sizeof(int *) * 3);
    grid[0] = (int *)malloc(sizeof(int) * 3);
    grid[1] = (int *)malloc(sizeof(int) * 3);
    grid[2] = (int *)malloc(sizeof(int) * 3);

    int i, j, k=1;
    for(i = 0; i < 3; i++) 
        for(j = 0; j < 3; j++)
            grid[i][j] = k++;

    assert(minPathSum(grid, 3, 3) == 21);

    return 0;
}
