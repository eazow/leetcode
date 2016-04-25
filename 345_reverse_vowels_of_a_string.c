#include <assert.h>
#include <string.h>

int isVowel(char c) {
    return c=='a'||c=='e'||c=='i'||c=='o'||c=='u'||c=='A'||c=='E'||c=='I'||c=='O'||c=='U';
}

char* reverseVowels(char* s) {
    int len = strlen(s);
    int i, j;
    char temp;
    for(i = 0, j = len-1; i < j; i++, j--) {
        while(!isVowel(s[i]) && i<len)
            i++;
        if(i == len)
            return s;
        while(!isVowel(s[j]) && j>=0)
            j--;

        if(i < j) {
            temp = s[i];
            s[i] = s[j];
            s[j] = temp;
        }
    }

    return s;
}

int main() {
    char s[] = "hello";

    assert(strcmp(reverseVowels(s), "holle") == 0); 

    return 0;
}
