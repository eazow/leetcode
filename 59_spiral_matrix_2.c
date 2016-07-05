#include <assert.h>
#include <stdlib.h>
#include <stdio.h>

int** generateMatrix(int n) {
    if(n == 0) return NULL;

    int** nums = (int**)malloc(sizeof(int *) * n);
    int i = 0;
    for(i = 0; i < n; i++) {
        nums[i] = (int *)malloc(sizeof(int) * n);
    }
    i = 0;
    int j = 0;
    int k = 1;
    int step = 0;
    while(k <= n*n && step<n) {
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
    nums[i][j] = k;

    return nums;
}

int main() {
    int** nums = generateMatrix(3);
    assert(nums[0][0] == 1);
    assert(nums[0][1] == 2);
    assert(nums[0][2] == 3);
    assert(nums[1][2] == 4);
    assert(nums[2][2] == 5);
    assert(nums[2][1] == 6);
    assert(nums[2][0] == 7);
    assert(nums[1][0] == 8);
    assert(nums[1][1] == 9);

    return 0;
}
