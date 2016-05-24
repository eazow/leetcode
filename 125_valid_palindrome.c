#include <assert.h>
#include <string.h>
#include <stdio.h>

int isAlphaOrDigit(char c) {
    return (c>='A'&&c<='Z') || (c>='a'&&c<='z') || (c>='0'&&c<='9');
}

int toLower(char c) {
    if(c>='A' && c<='Z') {
        return c+'a'-'A';
    }
    return c;
}

int isPalindrome(char* s) {
    int len = strlen(s);
    int i = 0, j = len-1;
    char first, last;
    for(; i < j; i++,j--) {
        while(!isAlphaOrDigit(s[i]) && i<j)
            i++;
        first = s[i];
        while(!isAlphaOrDigit(s[j]) && i<j)
            j--;
        last = s[j];
        if(toLower(first) != toLower(last))
            return 0;

    }
    return 1;
}

int main() {
    assert(isPalindrome("0P") == 0);
    assert(isPalindrome("abcba") == 1);
    assert(isPalindrome("A man, a plan, a canal: Panama") == 1);

    return 0;
}
