#include <assert.h>

#define min(A,B) ((A)<(B)?(A):(B))

char* getHint(char *secret, char* guess) {
    int i = 0;
    int aNum = 0;
    int hashSecret = (int *)malloc(sizeof(int)*10);
    int hashGuess = (int *)malloc(sizeof(int)*10);
    memset(hashSecret, 0, 10);
    memset(hashGuess, 0, 10);
    for(i = 0; secret[i] != '\0'; i++) {
        if(secret[i] == guess[i])
            aNum++;
        else {
            hashSecret[secret[i]]++;
            hashGuess[guess[i]]++;
        }
    }
    int bNum = 0;
    for(i = 0; i < 10; i++) {
        bNum += min(hashSecret[i], hashGuess[i]);
    }


}

int main() {

    return 0;
}
