#include <assert.h>

int isPalindrome(int x) {
    if(x < 0) return 0;
    if(x < 10) return 1;
    if(x%10==0) return 0;

    int left = x, right = 0;

    while(left) {
        right = 10*right+left%10;
        left = left/10;
    }
    return right==x?1:0;
}

int main() {
    assert(isPalindrome(121) == 1);
    assert(isPalindrome(-121) == 0);
}
