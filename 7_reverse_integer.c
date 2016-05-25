#include <assert.h>
#include <limits.h>

int reverse(int x) {
    long long result = 0;
    int negative = 0;
    while(x != 0) {
        result = result*10 + x%10;
        x /= 10;
    }
    return (result>INT_MAX || result<INT_MIN)? 0 : result;
}

int main() {
    assert(reverse(123) == 321);
    assert(reverse(-123) == -321);
    
    return 0;
}
