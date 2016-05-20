#include <assert.h>
#include <string.h>
#include <stdlib.h>

int binaryToDecimal(char* str) {
    int strLen = strlen(str);
    int i = 0;
    int sum = str[i]-'0';
    for(i = 1; i < strLen; i++) {
        sum <<= 1;
        sum += str[i]-'0';
    }
    return sum;
}

char* decimalToBinary(int num) {
    if(num == 0)
        return "0";
    char* str = (char *)malloc(sizeof(char) * 32);
    int i = 0;
    while(num) {
        str[i++] = (char)(num%2+'0');
        num >>= 1;
    }
    str[i] = '\0';
    int len = i;
    for(i = 0; i < len/2; i++) {
        int temp = str[i];
        str[i] = str[len-i-1];
        str[len-i-1] = temp;
    }
    return str;
}

char* addBinary(char* a, char* b) {
    return decimalToBinary(binaryToDecimal(a)+binaryToDecimal(b));
}

int main() {
    char *sum = addBinary("11" ,"1");
    assert(strcmp(sum, "100") == 0);

    return 0;
}
