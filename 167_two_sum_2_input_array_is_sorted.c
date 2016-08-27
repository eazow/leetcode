#include <assert.h>
#include <stdlib.h>

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int i = 0, j = i+1;
    for(i=0, j=i+1; i < numsSize-1; j++) {
        if(nums[i] + nums[j] == target) {
            return;
        }
        else if(nums[i] + nums[j] < target) {
            j++;
            if(j == numsSize)
                i++;
        }
        else
            return NULL;    
    }
}

int main() {


    return 0;
}
