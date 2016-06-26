#include <assert.h>
#include <stdlib.h>

int* grayCode(int n, int* returnSize) {
    int i = 0;
    int* nums = (int *)malloc(sizeof(int)*(1<<n));
    for(i = 0; i < (1<<n); i++) {
        nums[i] = i ^ (i >> 1);
    }
    *returnSize = 1<<n;
    return nums;
}

int main() {
    int returnSize = 0;
    int* nums = grayCode(2, &returnSize);
    assert(nums[0] == 0);
    assert(nums[1] == 1);
    assert(nums[2] == 3);
    assert(nums[3] == 2); 

    return 0;
}
