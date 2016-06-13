#include <assert.h>

int searchInsertRecursively(int* nums, int low, int high, int target) {
    if(low == high) {
        if(target > nums[low])
            return low+1;
        else if(target < nums[low])
            return low-1;
    }
    int middle = (low+high)/2;
    int num = nums[middle];
    if(target == num)
        return middle;
    else if(target > num)
        return searchInsertRecursively(nums, middle+1, high, target);
    return searchInsertRecursively(nums, low, middle-1, target);
}

int searchInsert(int* nums, int numsSize, int target) {
    return searchInsertRecursively(nums, 0, numsSize-1, target);
}
