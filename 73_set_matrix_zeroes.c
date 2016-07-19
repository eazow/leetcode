#include <assert.h>

void setZeroes(int** matrix, int matrixRowSize, int matrixColSize) {
    int i, j;
    int firstRow = 0, firstCol = 0;
    for(i = 0; i < matrixRowSize; i++) {
        for(j = 0; j < matrixColSize; j++) {
            if(matrix[i][j] == 0) {
                if(i == 0)
                    firstRow = 1;
                if(j == 0)
                    firstCol = 1;
                matrix[i][0] = 0;
                matrix[0][j] = 0;
            }
        }
    }
}


