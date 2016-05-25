#include <assert.h>

//Forward declaration of isBanVersion API.
int isBadVersion(int version);

int firstBadVersion(int n) {
    int left=1, right=n;
    int middle;
    while(left<right) {
//      middle = (left+right)/2;
        middle = left+(right-left)/2;
        if(isBadVersion(middle))
            right = middle;
        else
            left = middle+1;
    }

    return left;
}

int isBadVersion(int version) {
    return version>=3 ? 1 : 0;
}

int main() {
    assert(firstBadVersion(10) == 3);

    return 0;
}
