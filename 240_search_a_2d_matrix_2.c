#include <assert.h>
#include <stdlib.h>

int searchMatrix(int** matrix, int matrixRowSize, int matrixColSize, int target) {
    //search from top-right to left-bottom
    int i = 0, j = matrixColSize - 1;
    while(i < matrixRowSize && j >= 0) {
        if(target > matrix[i][j])
            i++;
        else if(target < matrix[i][j])
            j--;
        else
            return 1;
    }
    return 0;
}

int main() {
    int nums1[] = {1, 4, 7, 11, 15};
    int nums2[] = {2, 5, 8, 12, 19};
    int nums3[] = {3, 6, 9, 16, 22};
    int nums4[] = {10, 13, 14, 17, 24};
    int nums5[] = {18, 21, 23, 26, 30};
    int **matrix = (int **)malloc(sizeof(int *)*5);
    matrix[0] = nums1;
    matrix[1] = nums2;
    matrix[2] = nums3;
    matrix[3] = nums4;
    matrix[4] = nums5;

    assert(searchMatrix(matrix, 5, 5, 5) == 1);
    assert(searchMatrix(matrix, 5, 5, 20) == 0);

    return 0;
}
