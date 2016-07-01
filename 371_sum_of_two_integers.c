#include <assert.h>

int getSum(int a, int b) {
    return a+b;
}

int main() {
    assert(getSum(1,2) == 3);
    
    return 0;
}
