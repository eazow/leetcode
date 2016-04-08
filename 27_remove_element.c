#include <assert.h>

int removeElement(int *nums, int numsSize, int val) {
    int i = 0;
    int begin = 0;

    for(i =  0; i < numsSize; i++) {
        if(*(nums+i) != val)
            *(nums+begin++) = *(nums+i);
    }

    return begin;
}

int main() {

    int nums[4] = {3,2,2,3};
    int val = 3;

    assert(removeElement(nums, 4, val) == 2);
    assert(nums[0] == 2);

    return 0;
}
