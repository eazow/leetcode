#include <assert.h>
#include <stdlib.h>

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countBits(int num, int* returnSize) {
    int i = 0;
    int* bits = (int *)malloc(sizeof(int) * (num+1));
    bits[0] = 0;
    for(i = 0; i <= num; i++) {
        bits[i] = bits[i>>1] + (i&1);
    }
    *returnSize = num+1;
    return bits;
}

int main() {
    int returnSize = 0;
    int* bits = countBits(5, &returnSize);
    assert(bits[0] == 0);
    assert(bits[1] == 1);
    assert(bits[2] == 1);
    assert(bits[3] == 2);
    assert(bits[4] == 1);
    assert(bits[5] == 2);
    assert(returnSize == 6);

    return 0;
}
