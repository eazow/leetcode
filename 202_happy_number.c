#include <assert.h>

int getSquaresSum(int n) {
    int sum = 0;
    while(n > 0) {
        sum += (n%10) * (n%10);
        n = n/10;
    }
    return sum;
}

int isHappy(int n) {
    int map[10000] = {0};
    while(1) {
        n = getSquaresSum(n);
        if(n==1)
            return 1;
        if(!map[n])
            map[n] = 1;
        else 
            return 0;
    }
}

int main() {
    assert(isHappy(16) == 0);
    assert(isHappy(19) == 1);

    return 0;
}
