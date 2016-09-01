#include <assert.h>
#include <stdlib.h>

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
/**
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int i = 0, j = i+1;
    int* returnNums = NULL;
    for(i=0, j=i+1; i < numsSize-1;) {
        if(nums[i] + nums[j] == target) {
            returnNums = (int *)malloc(sizeof(int) * 2);
            returnNums[0] = i+1;
            returnNums[1] = j+1;
            *returnSize = 2;
            return returnNums;
        }
        else if(nums[i] + nums[j] < target) {
            j++;
            if(j == numsSize) {
                i++;
                j = i+1;
            }
        }
        else {
            i++;
            j = i+1;
        }
    }
    return returnNums;
}
*/

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int left = 0, right = numsSize-1;
    int* returnNums = NULL;
    int sum = 0;
    while(left < right) {
        sum = nums[left]+nums[right];
        if(sum == target) {
            returnNums = (int *)malloc(sizeof(int)*2);
            returnNums[0] = left+1;
            returnNums[1] = right+1;
            *returnSize = 2;
            break;
        }
        else if(sum > target)
            right--;
        else 
            left++;
    }
    return returnNums;
}

int main() {
    int nums[3] = {2,3,4};
    int returnSize = 0;
    int* returnNums = twoSum(nums, 3, 6, &returnSize);
    assert(returnNums[0] == 1);
    assert(returnNums[1] == 3);

    return 0;
}
