#include <assert.h>
#include <stdio.h>

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void printNums(int* nums, int numsSize) {
    int i = 0;
    for(i = 0; i < 10; i++)
        printf("%d ", nums[i]);
    puts("");
}

void sortColors(int* nums, int numsSize) {
    int i = 0, zeroIndex = 0, twoIndex = numsSize-1;
    for(i = 0; i < twoIndex; i++) {
        if(nums[i]==2)
            swap(nums+i, nums+twoIndex--);
        if(nums[i]==0 && i>zeroIndex)
            swap(nums+i, nums+zeroIndex++);
        printNums(nums, numsSize);
    }
}

int main() {
    int nums[10] = {1,1,0,0,2,0,1,1,2,0};
    sortColors(nums, 10);

    return 0;
}
