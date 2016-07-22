#include <assert.h>
#include <stdio.h>

int removeDuplicates(int* nums, int numsSize) {
    if(numsSize < 3)
        return numsSize;
    int i = 2;
    int count = 2;
    for(i = 2; i < numsSize; i++) {
        if(nums[i] > nums[count-2])
            nums[count++] = nums[i];
    }
    return count;
}

int main() {
    int nums[6] = {1,1,1,2,2,3};
    assert(removeDuplicates(nums, 6) == 5);
    assert(nums[2] == 2);
    assert(nums[4] == 3);

    return 0;
}
