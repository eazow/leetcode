#include <assert.h>
#include <stdlib.h>

int** generateMatrix(int n) {
    int** nums = (int**)malloc(sizeof(int *) * n);
    int i = 0;
    for(i = 0; i < n; i++) {
        nums[i] = (int *)malloc(sizeof(int) * n);
    }
    i = 0;
    int j = 0;
    int k = 1;
    int step = 0;
    while(k <= n*n) {
        //left to right
        while(j < n-step-1) 
            nums[i][j++] = k++;
        //top to bottom
        while(i < n-step-1)
            nums[i++][j] = k++;
        //right to left
        while(j > step)
            nums[i][j--] = k++;
        //bottom to top
        while(i > step+1) 
            nums[i--][j] = k++;
        step++;
    }

    return nums;
}

int main() {
    int** nums = generateMatrix(3);

    return 0;
}
