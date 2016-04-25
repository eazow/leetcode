#include <assert.h>
#include <string.h>
#include <stdlib.h>

char* reverseString(char* s) {
    int strLen = strlen(s);
    int i = 0;
    char* result = (char*)malloc(sizeof(char)*(strLen+1));
    for(i = 0; i < strLen; i++) {
        result[strLen-i-1] = s[i];
    }
    result[i] = '\0';

    return result;
}

int main() {
    assert(strcmp(reverseString("hello"), "olleh") == 0);

    return 0;
}
