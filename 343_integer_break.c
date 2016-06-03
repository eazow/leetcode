#include <assert.h>

int integerBreak(int n) {
    if(n == 2)
        return 1;
    else if(n == 3)
        return 2;
    int product = 1;
    while(n > 4) {
        product *= 3;
        n -= 3;
    }
    return product*n;
}

int main() {
    assert(integerBreak(2) == 1);
    assert(integerBreak(10) == 36);
    assert(integerBreak(50) == 86093442);

    return 0;
}
