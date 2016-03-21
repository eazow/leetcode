#include <assert.h>

int isPowerOfTwo(int n) {
    if(n == 0)
        return 0;

    while(n%2 == 0) 
        n /= 2;

    if(n == 1)
        return 1;
    return 0;
}

int main() {
    assert(isPowerOfTwo(8) == 1);
    assert(isPowerOfTwo(0) == 0);

    return 0;
}
