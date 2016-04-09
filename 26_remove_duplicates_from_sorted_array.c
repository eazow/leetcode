#include <assert.h>

int removeDuplicates(int *nums, int numsSize) {
    int i = 0;
    int begin = numsSize>0?1:0;

    for(i = 0; i < numsSize-1; i++) {
        if(nums[i+1] != nums[i])
            nums[begin++] = nums[i+1];
    }
    
    return begin;
}

int main() {
    int nums[3] = {1,1,2};

    assert(removeDuplicates(nums, 3) == 2);
    assert(nums[0] == 1);
    assert(nums[1] == 2);

    return 0;
}
