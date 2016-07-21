#include <assert.h>

int findPeakElement(int* nums, int numsSize) {
    int i;
    for(i = 1; i < numsSize; i++) {
        if(nums[i] < nums[i-1])
            return i-1;
    }
    return numsSize-1;
}

int main() {
    int nums[4] = {1,2,3,1};
    assert(findPeakElement(nums, 4) == 2);

    return 0;
}
