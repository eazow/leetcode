#include <assert.h>
#include <stdlib.h>
#include <stdio.h>

char* convertToTitle(int n) {

    char *title = (char *)malloc(sizeof(char)*32);
    int i = 31;
    title[i] = '\0';
    while(n > 0) {
        title[--i] = (n%26?n%26:26)+'A'-1;
        n /= 26;
    }
    return title+i;
}

int main() {
    convertToTitle(100);

    assert(strcmp(convertToTitle(52), "AZ") == 0);

    return 0;
}
