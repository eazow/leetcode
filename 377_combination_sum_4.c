#include <assert.h>

int combinationSum4(int* nums, int numsSize, int target) {
    if(target == 0)
        return 1;
    int i = 0;
    int result = 0;
    for(i = 0; i < numsSize; i++) {
        if(target >= nums[i])
            result += combinationSum4(nums, numsSize, target-nums[i]);
    }
    return result;
}

int main() {
    int nums[3] = {1,2,3};
    assert(combinationSum4(nums, 3, 4) == 7);

    return 0;
}
