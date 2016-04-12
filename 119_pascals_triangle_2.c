#include <assert.h>
#include <stdlib.h>

/**
 * Return an array of size *returnSize.
 * Node: The returned array must be alloced, assume caller calls free().
 */
int* getRow(int rowIndex, int* returnSize) {
    int* returnArray = calloc(rowIndex+1, sizeof(int));
    int i = 0, j = 0;
    for(i = 0; i <= rowIndex; i++) {
        for(j = rowIndex; j >= 0; j--) {
            if(j==0 || j==rowIndex)
                returnArray[j] = 1;
            else
                returnArray[j] += returnArray[j-1];
        }
    }
    *returnSize = rowIndex+1;
    return returnArray;
}

int main() {
    int returnSize = 0;
    int *row3 = getRow(3, &returnSize);
    assert(row3[1] == 3);
    assert(returnSize == 4);

    return 0;
}
