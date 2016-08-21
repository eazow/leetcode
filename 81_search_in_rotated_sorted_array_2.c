#include <assert.h>

int search(int* nums, int numsSize, int target) {
    int left = 0, right = numsSize-1;
    int middle;
    while(left <= right) {
        middle = left + (right-left)/2;
        if(nums[middle] == target)
            return 1;

    }
}

int main() {
    int nums[5] = {3,4,5,1,2};

    return 0;
}
