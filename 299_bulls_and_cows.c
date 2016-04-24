#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define min(A,B) ((A)<(B)?(A):(B))

char* getHint(char *secret, char* guess) {
    int i = 0;
    int aNum = 0;
    int *hashSecret = (int *)malloc(sizeof(int)*10);
    int *hashGuess = (int *)malloc(sizeof(int)*10);
    memset(hashSecret, 0, 10);
    memset(hashGuess, 0, 10);
    for(i = 0; secret[i] != '\0'; i++) {
        if(secret[i] == guess[i])
            aNum++;
        else {
            hashSecret[secret[i]-'0']++;
            hashGuess[guess[i]-'0']++;
        }
    }
    int bNum = 0;
    for(i = 0; i < 10; i++) {
        bNum += min(hashSecret[i], hashGuess[i]);
    }
    
    char s[1000];

    return (char *)s;
}

int main() {
    char *s = getHint("1807", "7810");

    return 0;
}
