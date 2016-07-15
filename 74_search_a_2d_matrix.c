#include <assert.h>
#include <stdlib.h>

int searchMatrix(int** matrix, int matrixRowSize, int matrixColSize, int target) {
    int left = 0;
    int right = matrixRowSize*matrixColSize-1;
    int middle = 0;

    while(left <= right) {
        middle = (left+right)/2;
        if(target > matrix[middle/matrixColSize][middle%matrixColSize]) 
            left = middle+1;
        else if(target < matrix[middle/matrixColSize][middle%matrixColSize])
            right = middle-1;
        else
            return 1;
    }
    return 0;
}

int main() {
    int nums0[4] = {1,3,5,7};
    int nums1[4] = {10,11,16,20};
    int nums2[4] = {23,30,34,50};
    int** matrix = (int **)malloc(sizeof(int *)*3);
    matrix[0] = nums0;
    matrix[1] = nums1;
    matrix[2] = nums2;
    assert(searchMatrix(matrix, 3, 4, 3)==1);
    assert(searchMatrix(matrix, 3, 4, 9)==0);

    return 0;
}
