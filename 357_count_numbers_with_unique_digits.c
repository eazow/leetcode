#include <assert.h>

/**
 * n = 0, count = 1
 * n = 1, count = 10
 * n = 2, count = 10 + 9*9
 * n = 3, count = 10 + 9*9 + 9*9*8
 * ...
 */
int countNumbersWithUniqueDigits(int n) {
    if(n == 0)
        return 1;
    if(n == 1)
        return 10;
    int count = 10;
    int i = 0;
    int product = 9;
    for(i = 1; i < n && i < 10; i++) {
        product *= 10-i;
        count += product;
    }
    return count;
}

int main() {
    assert(countNumbersWithUniqueDigits(0) == 1);
    assert(countNumbersWithUniqueDigits(1) == 10);
    assert(countNumbersWithUniqueDigits(2) == 91);
    assert(countNumbersWithUniqueDigits(10) == 8877691);
    assert(countNumbersWithUniqueDigits(100) == 8877691);

    return 0;
}
