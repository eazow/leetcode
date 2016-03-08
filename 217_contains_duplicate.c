#include <assert.h>
#include <stdlib.h>

int comp(const void *a, const void *b) {
    return *(int *)a-*(int *)b;
}

int containsDuplicate(int *nums, int numsSize) {
    int i = 0;
    qsort(nums, numsSize, sizeof(int), comp);
    for(i = 0; i < numsSize-1; i++) {
        if(nums[i] == nums[i+1])
            return 1;
    }
    return 0;
}

int main(int argc, char *argv[]) {
    int nums[5] = {1,2,3,2,1};
    assert(containsDuplicate(nums, 5) == 1);
    return 0;
}
