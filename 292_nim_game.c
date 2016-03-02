#include <stdio.h>

int canWinNim(int n) {
    return n%4!=0;
}

int main(int argc, char **argv) {
    printf("%d", canWinNim(4));
}
