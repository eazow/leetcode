#include <assert.h>
#include <stdlib.h>

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* singleNumber(int* nums, int numsSize, int* returnSize) {
    int i = 0;
    int result = 0;

    for(i = 0; i < numsSize; i++) {
        result ^= nums[i];
    }

//	int bit = result & (~(result-1));
    int bit = 1;
    while((result & 1) == 0) {
        bit <<= 1;
        result >>= 1;
    }

    int result1 = 0;
    int result2 = 0;
    for(i = 0; i < numsSize; i++) {
        if((nums[i] & bit) == 0)
            result1 ^= nums[i];
        else
            result2 ^= nums[i];
    }
    int* singleNums = (int *)malloc(sizeof(int)*2);
    singleNums[0] = result1;
    singleNums[1] = result2;
    *returnSize = 2;
    return singleNums;
}

int main() {
    int returnSize = 0;
    int nums[6] = {1,1,2,2,3,5};
    int* singleNums = singleNumber(nums, 6, &returnSize);
    assert(returnSize == 2);
    assert(singleNums[0] == 5);
    assert(singleNums[1] == 3);

    return 0;
}
