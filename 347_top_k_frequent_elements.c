#include <assert.h>
#include <stdlib.h>

void quicksort(int *nums, int low, int high) {
    if(low < high) {
        int key = nums[low];
        int left = low;
        int right = high;

        while(left < right) {
            while(left < right && key <= nums[right]) 
                right--;
            nums[left] = nums[right];

            while(left < right && key >= nums[left])
                left++;
            nums[right] = nums[left];
        }
        nums[left] = key;
        quicksort(nums, low, left-1);
        quicksort(nums, left+1, high);
    }
}

void sort(int* nums, int numsSize) {
    int i, j;
    int sorted = 1;
    for(i = 0; i < numsSize; i++) {
        sorted = 1;
        for(j = 0; j < numsSize-1; j++) {
            if(nums[j] > nums[j+1]) {
                int temp = nums[j];
                nums[j] = nums[j+1];
                nums[j+1] = temp;
                sorted = 0;
            }
        }
        if(sorted)
            break;
    }
}

void reverseSort(int* nums1, int* nums2, int numsSize) {
    int i, j;
    int sorted = 1;
    for(i = 0; i < numsSize; i++) {
        sorted = 1;
        for(j = 0; j < numsSize-1; j++) {
            if(nums1[j] < nums1[j+1]) {
                int temp = nums1[j];
                nums1[j] = nums1[j+1];
                nums1[j+1] = temp;
                sorted = 0;

                temp = nums2[j];
                nums2[j] = nums2[j+1];
                nums2[j+1] = temp;
            }
        }
        if(sorted)
            break;
    }
}

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* topKFrequent(int* nums, int numsSize, int k, int* returnSize) {
//  sort(nums, numsSize);
    quicksort(nums, 0, numsSize-1);
    int* statistics = (int *)malloc(sizeof(int) * numsSize);
    int i = 0;
    int sIndex = 0;
    statistics[sIndex] = 1;
    int* uniqueNums = (int *)malloc(sizeof(int) * numsSize);
    uniqueNums[sIndex] = nums[0];
    for(i = 1; i < numsSize; i++) {
        if(nums[i] == nums[i-1])
            statistics[sIndex]++;
        else {
            statistics[++sIndex] = 1;
            uniqueNums[sIndex] = nums[i];
        }
    }
    reverseSort(statistics, uniqueNums, sIndex+1);
    *returnSize = k;
    return uniqueNums;
}

int main() {
    int nums[6] = {1,1,1,2,2,3};
    int returnSize = 0;
    int* uniqueNums = topKFrequent(nums, 6, 2, &returnSize);
    assert(uniqueNums[0] == 1);
    assert(uniqueNums[1] == 2);
    assert(returnSize == 2);

    return 0;
}
