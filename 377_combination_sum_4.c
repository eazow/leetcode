#include <assert.h>
#include <stdlib.h>

/**
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
*/

int combinationSum4(int* nums, int numsSize, int target) {
    int* results = (int *)malloc(sizeof(int) * (target+1));
    int i = 0;
    int j = 0;
    results [0] = 1;
    for(i = 1; i <= target; i++)
        results[i] = 0;
    for(i = 0; i <= target; i++) {
        for(j = 0; j < numsSize; j++) {
            if(i >= nums[j])
                results[i] += results[i-nums[j]];
        }
    }
    return results[target];
}
int main() {
    int nums[3] = {1,2,3};
    assert(combinationSum4(nums, 3, 4) == 7);

    return 0;
}
