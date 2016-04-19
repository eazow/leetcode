#include <assert.h>

void merge(int* nums1, int m, int* nums2, int n) {
    int index = m+n-1;
    
    while(index >= 0) {
        if(n <= 0 || nums1[m-1] > nums2[n-1])
            nums1[index--] = nums1[--m];
        else 
            nums2[index--] = nums2[--n];
}

int main() {
    return 0;
}
