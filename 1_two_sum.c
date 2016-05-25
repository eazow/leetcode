#include <assert.h>
#include <stdlib.h>

int* sort(int* nums, int numsSize) {
    int *numsLocations = (int *)malloc(sizeof(int) * numsSize);
    int i = 0, j = 0;
    for(i = 0; i < numsSize; i++)
        numsLocations[i] = i;

    for(i = 0; i < numsSize; i++) {
        int sorted = 1;
        for(j = 0; j < numsSize-1; j++) {
            if(nums[j] > nums[j+1]) {
                int temp = nums[j];
                nums[j] = nums[j+1];
                nums[j+1] = temp;
                sorted = 0;
                temp = numsLocations[j];
                numsLocations[j] = numsLocations[j+1];
                numsLocations[j+1] = temp;
            }
        }
        if(sorted)
            break;
    }
    return numsLocations;
}

int find(int* nums, int num, int start, int end) {
    if(start > end)
        return -1;
    int i = (start+end)/2;
    if(num > nums[i])
        return find(nums, num, i+1, end);
    else if(num < nums[i]) 
        return find(nums, num, start, i-1);
    return i;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) {
    int *numsLocations = sort(nums, numsSize);
    int i = 0;
    int num;
    int *locations = (int *)malloc(sizeof(int) * 2);
    int j;
    for(i = 0; i < numsSize; i++) {
        num = nums[i];
        if((j=find(nums, target-num, i+1, numsSize-1)) >= 0) {
            locations[1] = numsLocations[j];
            locations[0] = numsLocations[i];
            return locations;
        }
    }
    return NULL;
}

int main() {
    int nums[4] = {2, 7, 11, 15};
    int *locations = twoSum(nums, 4, 9);
    assert(locations[0] == 0);
    assert(locations[1] == 1);

    int nums2[3] = {5, 75, 25};
    locations = twoSum(nums2, 3, 100);
    assert(locations[0] == 2);
    assert(locations[1] == 1);

    return 0;
}
