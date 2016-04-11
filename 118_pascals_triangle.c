#include <assert.h>
#include <stdlib.h>

/**
 * Return an array of arrays.
 * The sizes of the arrays are returned as *columnSizes Array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** generate(int numRows, int** columnSizes) {
    if(numRows <= 0)
        return NULL;
    int** returnArray = (int**)malloc(sizeof(int*) * numRows);
    *columnSizes = (int*)malloc(sizeof(int) * numRows);
    int line, col;
    for(line = 0; line < numRows; line++) {
        *(*columnSizes+line) = line+1;
        int *lineArray = (int *)malloc(sizeof(int) * (line+1));
        for(col = 0; col <= line; col++) {
            if(col==0 || col==line)
                lineArray[col] = 1;
            else
                lineArray[col] = returnArray[line-1][col-1] + returnArray[line-1][col];
        }
        returnArray[line] = lineArray;
    }
    return returnArray;
}

int main() {
    int *columnSizes = NULL;
    int **returnArray = generate(5, &columnSizes);
    assert(*returnArray[0] == 1);
    assert(*columnSizes == 1);

    return 0;
}
