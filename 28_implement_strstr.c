#include <assert.h>
#include <string.h>

int strStr(char* haystack, char* needle) {
    if(haystack==NULL || needle==NULL)
        return -1;

    int haystackLength = strlen(haystack);
    int needleLength = strlen(needle);
    if(needleLength > haystackLength)
        return -1;
    if(needleLength == 0)
        return 0;

    int i, j;
    for(i=0, j=0;  i < haystackLength; i++) {
        if(haystack[i] == needle[j]) {
            j++;
            if(j == needleLength)
                return i-j+1;
        }
        else {
            //important, 将i回溯到needle[0]出现的位置
            i = i-j;
            j = 0;
        }
    }
    return -1;
}

int main() {
    assert(strStr("abc", "a") == 0);
    assert(strStr("abcdef", "abcdefgh") == -1);
    assert(strStr("abcdef", "cde") == 2);
    assert(strStr("mississippi", "issip") == 4);

    return 0;
}
