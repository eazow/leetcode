#include <assert.h>
#include <stdlib.h>

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int *plusOne(int *digits, int digitsSize, int *returnSize) {
    int i = 0;
    for(i = digitsSize-1; i >= 0; i--) {
        if(*(digits+i) < 9) {
            digits[i]++;
            *returnSize = digitsSize;
            return digits;
        }
        *(digits+i) = 0;
    }
    *returnSize = digitsSize + 1;
    int *returnDigits = (int *)malloc(sizeof(int) * (digitsSize+1));
    *returnDigits = 1;
    for(i = 0; i < digitsSize; i++) 
        *(returnDigits+i+1) = *(digits+i);
    return returnDigits;
}

int main() {
    int digits[] = {1,2,3,4,5};
    int returnSize = 0;
    plusOne(digits, 5, &returnSize);
    assert(returnSize == 5);
}
