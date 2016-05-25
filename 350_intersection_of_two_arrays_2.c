#include <assert.h>
#include <stdlib.h>

void bubbleSort(int* nums, int numsSize) {
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

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* intersect(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
    bubbleSort(nums1, nums1Size);
    bubbleSort(nums2, nums2Size);

    int mallocSize = nums1Size<nums2Size?nums1Size:nums2Size;
    int* returnNums = (int *)malloc(sizeof(int) * (mallocSize));
    int i = 0, j = 0;
    while(i<nums1Size &&  j<nums2Size) {
        if(nums1[i] == nums2[j]) {
            returnNums[(*returnSize)++] = nums1[i];
            i++;
            j++;
        }
        else if(nums1[i] < nums2[j])
            i++;
        else
            j++;
    }
    return returnNums;
}

int main() {
    int nums1[] = {1,2,2,1};
    int nums2[] = {2,2};

    int returnSize = 0;
    int* nums = intersect(nums1, 4, nums2, 2, &returnSize);

    assert(returnSize == 2);
    assert(nums[0] == 2);
    assert(nums[1] == 2);
}
