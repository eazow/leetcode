#include <assert.h>
#include <stdlib.h>
#include <string.h>

char* intToRoman(int num) {
    int vals[] = {1000,900,500,400,100,90,50,40,10,9,5,4,1};
    char* strs[] = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
    
    char* roman = (char *)malloc(sizeof(char) * 100);
    int i = 0;
    int length = sizeof(vals)/sizeof(int);
    for(i = 0; i < length; i++) {
        while(num >= vals[i]) {
            strcat(roman, strs[i]);
            num -= vals[i];
        }
    }
    return roman;
}

int main() {
    assert(strcmp(intToRoman(9), "IX") == 0);

    return 0;
}
