#include <assert.h>

int findMin(int* nums, int numsSize) {
    int left = 0, right = numsSize-1;
    if(nums[left] < nums[right])
        return nums[left];

    int middle = 0;
    while(left < right) {
        middle = (left+right)/2;
        if(nums[middle] > nums[right])
            left = middle+1;
        else
            right = middle;
    }
    return nums[left];
}

int main() {
    int nums[8] = {4,5,6,7,0,1,2};
    assert(findMin(nums, 8) == 0);

    return 0;
}
