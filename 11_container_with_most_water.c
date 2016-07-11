#include <assert.h>

#define min(A,B) ((A)<(B)?(A):(B))
#define max(A,B) ((A)>(B)?(A):(B))

int maxArea(int* height, int heightSize) {
    int left = 0;
    int right = heightSize-1;
    int area = 0;
    while(left < right) {
        area = max(area, min(height[left],height[right])*(right-left));
        if(height[left] < height[right])
            left++;
        else
            right--;
    }
    return area;
}

int main() {
    int height[8] = {1,5,9,2,6,7,8,3};
    assert(maxArea(height, 8) == 32);

    return 0;
}
