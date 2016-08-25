#include <assert.h>

int search(int* nums, int numsSize, int target) {
    int left = 0, right = numsSize-1;
    int middle;
    while(left <= right) {
        middle = left + (right-left)/2;
        if(nums[middle]==target || nums[left]==target || nums[right]==target)
            return 1;
        //1,2,3,4,5
        if(nums[left] < nums[right]) {
            if(target > nums[middle])
                left = middle+1;
            else
                right = middle-1;
        }
        //4,5,6,1,2
        else if(nums[left] < nums[middle]) {
            if(target > nums[middle] || target < nums[left])
                left = middle + 1;
            else
                right = middle - 1;
        }
        //4,5,1,2,3
        else if(nums[left] > nums[middle]){
            if(target > nums[middle] && target < nums[right])
                left = middle + 1;
            else 
                right = middle - 1;
        }
        else
            right--;
    }
    return 0;
}

int main() {
    int nums[5] = {3,4,5,1,2};
    assert(search(nums, 5, 3) == 1);

    int nums2[5] = {1,3,1,1,1};
    assert(search(nums2, 5, 3) == 1);

    int nums3[3] = {5,1,3};
    assert(search(nums3, 3, 3) == 1);

    int nums4[4] = {1,1,3,1};
    assert(search(nums4, 4, 3) == 1);

    return 0;
}
