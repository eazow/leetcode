#include <assert.h>

int rangeBitwiseAnd(int m, int n) {
    int bits = 1;
    while(m != n) {
        m >>= 1;
        n >>= 1;
        bits <<= 1;
    }
    return m*bits;
}

/**
int rangeBitwiseAnd(int m, int n) {
    int bitwiseAnd = m;
    while(m <= n) {
        bitwiseAnd &= m;
        m++;
    }
    return bitwiseAnd;
}
*/

int main() {
    assert(rangeBitwiseAnd(5,7) == 4);
    assert(rangeBitwiseAnd(1,3) == 0);

    return 0;
}
