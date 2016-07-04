#include <assert.h>

int getSum(int a, int b) {
    int sum = 0;
    int i = 0;
    int carry = 0;
    int bitSum = 0;
    while(i < 32) {
        bitSum = (a&1)+(b&1)+carry;
        carry = bitSum/2;
        sum |= ((bitSum%2)<<i);
        a>>=1;
        b>>=1;
        i++;
    }
    return sum;
}

int main() {
    assert(getSum(1,2) == 3);
    assert(getSum(60, 20) == 80);

    return 0;
}
