#include <assert.h>
#include <stdlib.h>

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    int i = 0;
    int product = 1;
    int* products = (int *)malloc(sizeof(int) * numsSize);
    for(i = 0; i < numsSize; i++) {
        products[i] = product;
        product *= nums[i];
    }
    product = 1;
    for(i = numsSize-1; i >= 0; i--) {
        products[i] *= product;
        product *= nums[i];
    }
    *returnSize = numsSize;
    return products;
}

int main() {
    int nums[4] = {1,2,3,4};
    int returnSize = 0;
    int* products = productExceptSelf(nums, 4, &returnSize);
    assert(returnSize == 4);
    assert(products[0] == 24);
    assert(products[1] == 12);
    assert(products[2] == 8);
    assert(products[3] == 6);

    return 0;
}
