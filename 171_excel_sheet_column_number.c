#include <assert.h>
#include <string.h>

/**
int titleToNumber(char *s) {
    int i = 0;
    int column = 0;
    int step = 1;
    for(i = strlen(s)-1; i >= 0; i--) {
        column += (*(s+i)-'A'+1)*step;
        step *= 26;
    }
    return column;
}*/

int titleToNumber(char *s) {
    int i = 0;
    int column = 0;
    for(i = 0; i < strlen(s); i++) {
        column = column*26+*(s+i)-'A'+1;
    }
    return column;
}

int main(int argc, char *argv[]) {
    assert(titleToNumber("A") == 1);
    assert(titleToNumber("AA") == 27);
    assert(titleToNumber("AAA") == 703);
}
