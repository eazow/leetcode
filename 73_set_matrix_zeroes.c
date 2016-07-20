#include <assert.h>
#include <stdlib.h>

void setZeroes(int** matrix, int matrixRowSize, int matrixColSize) {
    int i, j;
    int firstRow = 0, firstCol = 0;
    for(i = 0; i < matrixRowSize; i++) {
        for(j = 0; j < matrixColSize; j++) {
            if(matrix[i][j] == 0) {
                if(i == 0)
                    firstRow = 1;
                else
                    matrix[i][0] = 0;
                if(j == 0)
                    firstCol = 1;
                else
                    matrix[0][j] = 0;
            }
        }
    }
    for(j = 1; j < matrixColSize; j++) {
        if(matrix[0][j] == 0) {
            for(i = 0; i < matrixRowSize; i++) 
                matrix[i][j] = 0;
        }
    }
    for(i = 1; i < matrixRowSize; i++) {
        if(matrix[i][0] == 0) {
            for(j = 0; j < matrixColSize; j++)
                matrix[i][j] = 0;
        }
    }
    if(firstRow) {
        for(j = 0; j < matrixColSize; j++)
            matrix[0][j] = 0;
    }
    if(firstCol) {
        for(i = 0; i < matrixRowSize; i++)
            matrix[i][0] = 0;
    }
}

int main() {
    int nums0[3] = {1,2,3};
    int nums1[3] = {0,5,6};
    int nums2[3] = {7,8,9};
    int** matrix = (int **)malloc(sizeof(int *)*3);
    matrix[0] = nums0;
    matrix[1] = nums1;
    matrix[2] = nums2;

    setZeroes(matrix, 3, 3);

    assert(matrix[0][0] == 0);
    assert(matrix[0][1] == 2);
    assert(matrix[0][2] == 3);
    assert(matrix[1][0] == 0);
    assert(matrix[1][1] == 0);
    assert(matrix[1][2] == 0);
    assert(matrix[2][0] == 0);
    assert(matrix[2][1] == 8);
    assert(matrix[2][2] == 9);

    return 0;
}
