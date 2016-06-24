#include <assert.h>
#include <stdlib.h>
#include <stdio.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *columnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** combinationSum3(int k, int n, int** columnSizes, int* returnSize) {
    int nums[6] = {0};

    int num = 0;
    int sum = 0;
    int top = 0;
    while(1) {
        num++;
        nums[top++] = num;
        if(num > n && top==1)
            return NULL;
        sum += num;
        if(sum == n && top == k) {
            printf("1\n");
            num = nums[--top];
            sum -= num;
        }
        else if(top == k) {
            num = nums[--top];
            sum -= num;
            while(num == n-1) {
                num = nums[--top];
                sum -= num;
                if(top == 0 && num==n)
                    return NULL;
            }
        }
    }

}


int main() {
    combinationSum3(3, 8, NULL, NULL);
    return 0;
}
