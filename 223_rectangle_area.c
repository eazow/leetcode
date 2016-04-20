#include <assert.h>

void sort(int *nums, int length) {
    int i = 0, j = 0;

    for(i = 0; i < length; i++) {
        for(j = 0; j < length-1; j++) {
            if(nums[j] > nums[j+1]) {
                int temp = nums[j+1];
                nums[j+1] = nums[j];
                nums[j] = temp;
            }
        }
    }
}

int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
    int nums1[4] = {A, C, E, G};
    sort(nums1, 4);
    int length = nums1[2] - nums1[1];
    int nums2[4] = {B, D, F, H};
    sort(nums2, 4);
    int width = nums2[2] - nums2[1];

    return length * width;
}

int main() {
    assert(computeArea(-3, 0, 3, 5, 0, -1, 9, 2) == 6);

    return 0;
}
