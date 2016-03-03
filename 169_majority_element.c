#include <assert.h>

int majorityElement(int *nums, int numsSize) {
    int i = 0;
    int majority = nums[0];
    int count = 1;
    for(i = 1; i < numsSize; i++) {
        if(count == 0) { 
            majority = nums[i];
            count = 1;
        }
        else if(nums[i] == majority)
            count++;
        else
            count--;
    }
    return majority;
}

int main(int argc, char *argv[]) {
    int nums[7] = {2,2,1,1,1,2,2};
    assert(majorityElement(nums, 7) == 2);
}
