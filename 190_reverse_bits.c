#include <assert.h>
#include <stdint.h>

uint32_t reverseBits(uint32_t n) {
    uint32_t m = 0;
    int i = 0;
    for(i = 0; i < 32; i++,n>>=1) {
        m = m << 1;
        m = m | (n & 1);
    }
    return m;
}

int main() {
    assert(reverseBits(43261596) == 964176192);

    return 0;
}
