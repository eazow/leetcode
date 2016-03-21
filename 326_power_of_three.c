#include <math.h>
#include <assert.h>

int isPowerOfThree(int n) {
    if(n <= 0)
        return 0;
    int MAX_POWER_OF_THREE = (int)pow(3, 19);
    if(MAX_POWER_OF_THREE % n ==0)
        return 1;
    return 0;
}

int main() {
    assert(isPowerOfThree(-3) == 0);
    assert(isPowerOfThree(27) == 1);
    assert(isPowerOfThree(0) == 0);

    return 0;
}
