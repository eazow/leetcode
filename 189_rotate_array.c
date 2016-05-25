#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

void rotate(int* nums, int numsSize, int k) {
    k %= numsSize;
    if(k > 0) {
        int* tempNums = (int *)malloc(sizeof(int) * k);
        int i;
        for(i = 0; i < k; i++)
            tempNums[i] = nums[numsSize-k+i];
        for(i = numsSize-k-1; i >=0; i--)
            nums[i+k] = nums[i];
        for(i = 0; i < k; i++)
            nums[i] = tempNums[i];
    }
}

int main() {
    int nums[7] = {1,2,3,4,5,6,7};
    rotate(nums, 7, 3);
    assert(nums[0] == 5);
    assert(nums[1] == 6);
    assert(nums[2] == 7);
    assert(nums[3] == 1);
    assert(nums[4] == 2);
    assert(nums[5] == 3);
    assert(nums[6] == 4);

    int nums2[6] = {1,2,3,4,5,6};
    rotate(nums2, 6, 11);
    assert(nums2[0] == 2);
    assert(nums2[1] == 3);
    assert(nums2[2] == 4);
    assert(nums2[3] == 5);
    assert(nums2[4] == 6);
    assert(nums2[5] == 1);
    
    return 0;
}
