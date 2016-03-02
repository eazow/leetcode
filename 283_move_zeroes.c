#include <assert.h>
#include <stdio.h>

void moveZeroes(int *nums, int numsSize) {
    int zeroIndex=0, i=0;

    for(i = 0; i < numsSize; i++) {
        if(*(nums+i) != 0) {
            if(i>zeroIndex) {
                *(nums+zeroIndex) = *(nums+i);
                *(nums+i) = 0;
            }
            zeroIndex++;
        }
        else {
            continue;
        }
    }
}

void printArray(int *nums, int numsSize) {
    int i = 0;
    printf("[");
    for(i = 0; i < numsSize; i++) {
        printf("%d ", *(nums+i));
    }
    printf("]\n");

}

int main(int argc, char *argv[]) {
    int nums[6] = {1,0,2,3,4,5};
    moveZeroes(nums, 6);
    printArray(nums, 6);
    assert(nums[0] == 1);
    assert(nums[1] == 2);
    assert(nums[2] == 3);
    assert(nums[3] == 4);
    assert(nums[4] == 5);
    assert(nums[5] == 0);
}
