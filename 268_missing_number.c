#include <assert.h>

int missingNumber(int* nums, int numsSize) {
    int expectedSum = (1+numsSize)*numsSize/2;
    int i = 0;
    int sum = 0;
    for(i = 0; i < numsSize; i++) {
        sum += nums[i];
    }
    return expectedSum - sum;
}

int main() {
    int nums[3] = {0, 1, 3};
    assert(missingNumber(nums, 3) == 2);

    return 0;
}
