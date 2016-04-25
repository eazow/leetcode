#include <assert.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

#define min(A,B) ((A)<(B)?(A):(B))

char* getHint(char *secret, char* guess) {
    int i = 0;
    int aNum = 0;
    int hashSecret[10] = {0};
    int hashGuess[10] = {0};
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
    
    char *s = (char *)malloc(sizeof(char) * 100);
    sprintf(s, "%dA%dB", aNum, bNum);

    return s;
}

int main() {
    char *s = getHint("1807", "7810");

    assert(s[0] == '1');
    assert(s[2] == '3');

    return 0;
}
