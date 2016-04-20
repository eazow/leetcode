#include <assert.h>

void merge(int* nums1, int m, int* nums2, int n) {
    int index = m+n-1;
    m--;
    n--;
    while(index >= 0) {
        if((m >= 0 && nums1[m] > nums2[n]) || n < 0)
            nums1[index--] = nums1[m--];
        else
            nums1[index--] = nums2[n--];
    }
}

int main() {
    int num1[9] = {1,3,5,7,9,0,0,0,0};
    int num2[4] = {2,4,6,8};

    merge(num1, 5, num2, 4);

    assert(num1[0] == 1);
    assert(num1[1] == 2);

    return 0;
}
