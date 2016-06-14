#include <assert.h>

int searchInsertRecursively(int* nums, int low, int high, int target) {
    if(low > high)
        return low;
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

int main() {
    int nums[4] = {1,3,5,6};
    assert(searchInsert(nums, 4, 5) == 2);
    assert(searchInsert(nums, 4, 2) == 1);
    assert(searchInsert(nums, 4, 7) == 4);
    assert(searchInsert(nums, 4, 0) == 0);

    return 0;
}
