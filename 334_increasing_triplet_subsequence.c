#include <assert.h>
#include <limits.h>

int increasingTriplet(int* nums, int numsSize) {
    int i = 0;
    int small = INT_MAX, big = INT_MAX;
    
    for(i = 0; i < numsSize; i++) {
        if(nums[i] <= small)
            small = nums[i];
        else if(nums[i] <= big)
            big = nums[i];
        else
            return 1;
    }
    return 0;
}

int main() {
    int nums[5] = {1,2,3,4,5};
    assert(increasingTriplet(nums, 5) == 1);

    int nums2[5] = {3,2,1,5,4};
    assert(increasingTriplet(nums2, 5) == 0);

    return 0;
}
