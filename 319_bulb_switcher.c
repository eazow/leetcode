#include <assert.h>
#include <stdlib.h>

int bulbSwitch(int n) {
    int* nums = (int *)calloc(sizeof(int), n);
    int i, j, num;
    for(i = 1; i <= n; i++)
        for(j = 1; j*i <= n; j++) {
            num = nums[j*i-1];
            nums[j*i-1] = (~num)&1;
        }
    int count = 0;
    for(i = 0; i < n; i++)
        if(nums[i] == 1)
            count++;

    return count;
}

int main() {
    assert(bulbSwitch(3) == 1);
    assert(bulbSwitch(9999999) == 3162);

    return 0;
}
