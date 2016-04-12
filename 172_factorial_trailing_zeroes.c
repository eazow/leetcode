#include <assert.h>

int trailingZeroes(int n) {
    int count = 0;

    while(n/5>=1) { 
        count += n/5;
        n = n/5;
    }

    return count;
}

int main() {
    assert(trailingZeroes(5) == 1);
    assert(trailingZeroes(10) == 2);

    return 0;
}
