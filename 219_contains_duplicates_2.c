#include <assert.h>
#include <stdlib.h>
#include <string.h>

int containsNearbyDuplicate(int* nums, int numsSize, int k) {
    int min = nums[0], max = nums[0];

    int i = 0;
    for(i = 0; i < numsSize; i++) {
        if(nums[i] < min)
            min = nums[i];
        else if(nums[i] > max)
            max = nums[i];
    }

    int* hashmap = (int *)malloc(sizeof(int) * (max-min+1));
    memset(hashmap, -1, max-min+1);
    for(i = 0; i < numsSize; i++) {
        int num = nums[i];
        if(hashmap[num-min] == -1)
            hashmap[num-min] = i;
        else if(i-hashmap[num-min] <= k)
            return 1;
        hashmap[num-min] = i;
    }

    return 0;
}

int main() {
    int nums[5] = {1,10,20,30,1};

    assert(containsNearbyDuplicate(nums, 5, 5) == 1);
    assert(containsNearbyDuplicate(nums, 5, 2) == 0);


    return 0;
}
