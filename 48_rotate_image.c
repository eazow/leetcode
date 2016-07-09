#include <assert.h>
#include <stdlib.h>

void rotate(int** matrix, int matrixRowSize, int matrixColSize) {
    int i, j;
    for(i = 0; i < matrixRowSize; i++) {
        for(j = 0; j < i; j++) {
            int temp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = temp;
        }
    }
    for(i = 0; i < matrixRowSize; i++) {
        for(j = 0; j < matrixColSize/2; j++) {
            int temp = matrix[i][j];
            matrix[i][j] = matrix[i][matrixColSize-j-1];
            matrix[i][matrixColSize-j-1] = temp;
        }
    }
}

int main() {
    int** matrix = (int **)malloc(sizeof(int *)*3);
    int nums0[] = {1,2,3};
    int nums1[] = {4,5,6};
    int nums2[] = {7,8,9};
    matrix[0] = nums0;
    matrix[1] = nums1;
    matrix[2] = nums2;
    rotate(matrix, 3, 3);

    assert(matrix[0][0] == 7);
    assert(matrix[0][1] == 4);
    assert(matrix[0][2] == 1);
    assert(matrix[1][0] == 8);
    assert(matrix[1][1] == 5);
    assert(matrix[1][2] == 2);
    assert(matrix[2][0] == 9);
    assert(matrix[2][1] == 6);
    assert(matrix[2][2] == 3);

    return 0;
}
