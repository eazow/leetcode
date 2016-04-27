#include <assert.h>
#include <string.h>

int lengthOfLastWord(char* s) {
    int strLen = strlen(s);
    int i = 0;

    int len = 0;
    char c;
    for(i = strLen-1; i >= 0; i--) {
        c = s[i];
        if(len==0 && c==' ')
            continue;
        else if(c == ' ')
            break;
        len++;
    }
    return len;
}

int main() {
    assert(lengthOfLastWord("hello") == 5);
    assert(lengthOfLastWord("   ") == 0);
    assert(lengthOfLastWord("  hello world  ") == 5);

    return 0;
}
