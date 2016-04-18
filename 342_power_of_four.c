#include <assert.h>

int isPowerOfFour(int num) {
    return (num>0) && ((num&0x55555555)==num) && ((num&(num-1))==0);
}

int main() {
    assert(isPowerOfFour(16) == 1);
    assert(isPowerOfFour(20) == 0);

    return 0;
}
