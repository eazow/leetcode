#include <assert.h>
#include <limits.h>

int myAtoi(char* str) {
    while(*str == ' ')
        str++;
    int sign = 1;
    if(*str == '-') {
        sign = -1;
        str++;
    }
    else if(*str == '+') 
        str++;
    int result = 0;
    while(*str != '\0') {
        if(*str>='0' && *str<='9') {
            if((result > INT_MAX/10) || (result==INT_MAX/10 && *str>'7')) {
                if(sign == 1)
                    return INT_MAX;
                return INT_MIN;
            }
            result = result*10 + *str-'0';
        }
        else
            return sign*result;
        str++;
    }
    return sign*result;
}

int main() {
    assert(myAtoi("123111111") == 123111111);
    assert(myAtoi("a1") == 0);
    assert(myAtoi("      111111111111111111111") == INT_MAX);
    assert(myAtoi("-111111111111111111111111111") == INT_MIN);
    assert(myAtoi("123aaa") == 123);
    assert(myAtoi("-1") == -1);
    assert(myAtoi("+-2") == 0);

    return 0;
}
