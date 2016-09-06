#include <assert.h>

int rangeBitwiseAnd(int m, int n) {
    int bitwiseAnd = m;
    while(m <= n) {
        bitwiseAnd &= m;
        m++;
    }
    return bitwiseAnd;
}

int main() {
    assert(rangeBitwiseAnd(5,7) == 4);

    return 0;
}
