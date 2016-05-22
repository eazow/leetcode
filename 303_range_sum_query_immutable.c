#include <assert.h>
#include <stdlib.h>

struct NumArray {
    int* nums;
    int* sums;
    int numsSize;
};

/** Initialize your data structure here. */
struct NumArray* NumArrayCreate(int* nums, int numsSize) {
    struct NumArray* numArray = (struct NumArray*)malloc(sizeof(struct NumArray));
    numArray->sums = (int *)malloc(sizeof(int) * numsSize);
    numArray->nums = nums;
    numArray->numsSize = numsSize;
    int i = 0;
    int sum = 0;
    for(i = 0; i < numsSize; i++) {
        sum += nums[i];
        numArray->sums[i] = sum;
    }

    return numArray;
}

int sumRange(struct NumArray* numArray, int i, int j) {
    if(i == 0)
        return numArray->sums[j];
    return numArray->sums[j] - numArray->sums[i-1];
}

/** Deallocates memory previously allocated for the data structure. */
void NumArrayFree(struct NumArray* numArray) {
//  free(numArray->nums);
    free(numArray->sums);
    free(numArray);
}

// Your NumArray object will be instantiated and called as such:
// struct NumArray* numArray = NumArrayCreate(nums, numsSize);
// sumRange(numArray, 0, 1);
// sumRange(numArray, 1, 2);
// NumArrayFree(numArray);
int main() {
    int nums[6] = {-2, 0, 3, -5, 2, -1};
    struct NumArray* numArray = NumArrayCreate(nums, 6);
    assert(sumRange(numArray, 0, 2) == 1);
    assert(sumRange(numArray, 2, 5) == -1);
    assert(sumRange(numArray, 0, 5) == -3);
    NumArrayFree(numArray);

    return 0;
}
