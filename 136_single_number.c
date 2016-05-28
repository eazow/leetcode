#include <assert.h>

int singleNumber(int* nums, int numsSize) {
    int i = 0;
    int single = 0;
    for(i = 0; i < numsSize; i++) {
        single ^= nums[i];
    }
    return single;
}

int main() {
    int nums[5] = {1,3,3,1,5};
    assert(singleNumber(nums, 5) == 5);

    return 0;
}
