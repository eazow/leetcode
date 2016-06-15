#include <assert.h>

int singleNumber(int* nums, int numsSize) {
    int i = 0;
    int j = 0;
    int sum = 0;
    int singleNumber = 0;
    for(i = 0; i < 32; i++) {
        sum = 0;
        for(j = 0; j < numsSize; j++)
            sum += ((nums[j] >> i) & 1);
        singleNumber |= ((sum % 3) << i);
    }
    return singleNumber;
}

int main() {
    int nums[7] = {1,1,1,2,2,2,3};
    assert(singleNumber(nums, 7) == 3);

    return 0;
}
