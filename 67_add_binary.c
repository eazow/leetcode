#include <assert.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

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
//  return decimalToBinary(binaryToDecimal(a)+binaryToDecimal(b));

    int lenA = strlen(a);
    int lenB = strlen(b);
    int len = lenA>lenB?lenA:lenB;
    char *sum = (char *)malloc(sizeof(char) * (len+2));
    sum[len+1] = '\0';
    int bitSum = 0;
    while(len >= 0) {
        if(lenA > 0)
            bitSum += a[--lenA]-'0';
        if(lenB > 0)
            bitSum += b[--lenB]-'0';
        sum[len--] = (bitSum&0x01)+'0';
        bitSum >>= 1;
    }
    if(sum[0]!='0')
        return sum;
    return &sum[1];
}

int main() {
    assert(strcmp(addBinary("11", "1"), "100") == 0);
    assert(strcmp(addBinary("100", "1"), "101") == 0);
    assert(strcmp(addBinary("111111111100000000001111111111000000000011111111110000000000", "1"), "111111111100000000001111111111000000000011111111110000000001") == 0);

    return 0;
}
