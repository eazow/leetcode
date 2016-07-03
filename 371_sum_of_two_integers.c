#include <assert.h>

int getSum(int a, int b) {
    int carry = 0;
    return a+b;
}

int main() {
    assert(getSum(1,2) == 3);
    assert(getSum(60, 20) == 80);

    return 0;
}
