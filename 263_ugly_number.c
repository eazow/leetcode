#include <assert.h>

int isUgly(int num) {
    if(num == 0)
        return 0;

    while(num%2==0) num/=2;
    while(num%3==0) num/=3;
    while(num%5==0) num/=5;
    
    if(num==1)
        return 1;
    return 0;
}

int main() {
    assert(isUgly(0) == 0);
    assert(isUgly(2) == 1);
    assert(isUgly(3) == 1);
    assert(isUgly(5) == 1);
    assert(isUgly(14) == 0);

    return 0;
}
