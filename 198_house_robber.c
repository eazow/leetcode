#include <assert.h>
#include <stdlib.h>

#define max(a,b) (a)>(b)?(a):(b)

/**
 * Time Limit Exceeded
 *
int rob(int *nums, int numsSize) {
    if(numsSize == 0)
        return 0;
    else if(numsSize == 1)
        return nums[0];
    else if(numsSize <= 2)
        return max(nums[0], nums[1]);

    return max(rob(nums, numsSize-2)+nums[numsSize-1], rob(nums, numsSize-1));
}
 */

int rob(int *nums, int numsSize) {
    if(numsSize == 0)
        return 0;
    else if(numsSize == 1)
        return nums[0];

    int *max = malloc(sizeof(int) * numsSize);
    max[0] = nums[0];
    max[1] = max(nums[0], nums[1]);
    int i = 0;
    for(i = 2; i < numsSize; i++) {
        max[i] = max(max[i-2]+nums[i], max[i-1]);
    }

    return max[numsSize-1];
}

int main() {
    int nums[] = {1,10,2,5,6,8,3,9};
 
    assert(rob(nums, 8)==32);

    return 0;
}
