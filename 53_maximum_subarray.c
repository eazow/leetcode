#include <assert.h>

#define max(A,B) ((A)>(B)?(A):(B))

int maxSubArray(int* nums, int numsSize) {
    int i = 0;
    int maxSum = nums[i];
    int maxEnddingWithI = nums[i];
    for(i = 1; i < numsSize; i++) {
        maxEnddingWithI = max(maxEnddingWithI+nums[i], nums[i]);
        maxSum = max(maxSum, maxEnddingWithI);
    }
    return maxSum;
}

int main() {
    int nums[9] = {-2,1,-3,4,-1,2,1,-5,4};
    assert(maxSubArray(nums, 9) == 6);

    return 0;
}
