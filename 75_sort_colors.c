#include <assert.h>

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int compareArrays(int* nums1, int* nums2, int numsSize) {
    int i = 0;
    for(i = 0; i < numsSize; i++) {
        if(nums1[i] != nums2[i])
            return 1;
    }
    return 0;
}

void sortColors(int* nums, int numsSize) {
    int i = 0, zeroIndex = 0, twoIndex = numsSize-1;
    for(i = 0; i <= twoIndex; i++) {
        if(nums[i]==2)
            swap(nums+i--, nums+twoIndex--);
        else if(nums[i]==0) {
            if(i > zeroIndex)
                swap(nums+i, nums+zeroIndex++);
            else
                zeroIndex++;
        }
    }
}

int main() {
    int nums[3] = {0,1,0};
    int sortedNums[3] = {0,0,1};
    sortColors(nums, 3);
    assert(compareArrays(nums, sortedNums, 3) == 0);

    int nums2[6] = {1,2,0,0,2,1};
    int sortedNums2[6] = {0,0,1,1,2,2};
    sortColors(nums2, 6);
    assert(compareArrays(nums2, sortedNums2, 6) == 0);

    return 0;
}
