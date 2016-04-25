#include <assert.h>
#include <string.h>
#include <stdio.h>

char* reverseString(char* s) {
    int len = strlen(s);
    int i = 0;
    char temp;
    for(i = 0; i < len/2; i++) {
        temp = s[i];
        s[i] = s[len-i-1];
        s[len-i-1] = temp;
    }

    return s;
}

int main() {
    char s[] = "hello";
    char *str = "olleh";
    assert(strcmp(reverseString(s), str) == 0);

    return 0;
}
