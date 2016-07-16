#include <assert.h>

void quickSort(int* nums, int low, int high) {
    if(low < high) {
        int left = low;
        int right = high;
        int key = nums[low];

        while(left < right) {
            while(left < right && nums[right]>=key)
                right--;
            nums[left] = nums[right];
            while(left < right && nums[left]<=key)
                left++;
            nums[right] = nums[left];
        }
        nums[left] = key;
        quickSort(nums, low, left-1);
        quickSort(nums, low+1, high);
    }
}

int findKthLargest(int* nums, int numsSize, int k) {
    quickSort(nums, 0, numsSize-1);
    return nums[numsSize-k];
}

int main() {
    int nums[] = {3,2,1,5,6,4};
    assert(findKthLargest(nums, 6, 2) == 5);

    return 0;
}
