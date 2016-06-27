#include <assert.h>

int isPerfectSquare(int num) {
    int i = 0;
    for(i = 1; num > 0; i+=2) {
        num = num-i;
    }
    return num == 0;
}

int main() {
    assert(isPerfectSquare(9) == 1);
    assert(isPerfectSquare(100) == 1);
    assert(isPerfectSquare(101) == 0);

    return 0;
}
