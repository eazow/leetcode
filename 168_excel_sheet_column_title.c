#include <assert.h>
#include <stdlib.h>
#include <string.h>

char* convertToTitle(int n) {
    char *title = (char *)malloc(sizeof(char)*16);
    int i = 15;
    title[i] = '\0';
    while(n > 0) {
        title[--i] = (n-1)%26+'A';
        n = (n-1)/26;
    }
    return title+i;
}

int main() {
    assert(strcmp(convertToTitle(100), "CV") == 0);
    assert(strcmp(convertToTitle(52), "AZ") == 0);

    return 0;
}
