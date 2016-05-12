#include <assert.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

#define min(A,B) ((A)<(B)?(A):(B))

char *longestCommonPrefix(char** strs, int strsSize) {
    if(strsSize <= 0) 
        return "";
    char *str0 = strs[0];
    int prefixLen = strlen(str0);
    int i,j;
    for(i = 1; i < strsSize; i++) {
        int strLen = min(prefixLen, strlen(strs[i]));
        char *str = strs[i];
        int tempPrefixLen = 0;
        for(j = 0; j < strLen; j++) {
           if(str[j] == str0[j])
               tempPrefixLen++;
           else
               break;
        }
        prefixLen = min(tempPrefixLen, prefixLen);
    }

    char *returnStr = (char *)malloc(sizeof(char) * (prefixLen+1));
    for(i = 0; i < prefixLen; i++)
        returnStr[i] = str0[i];
    returnStr[i] = '\0';

    return returnStr;
}

int main() {
    char *strs[10] = {
        "abcdefg",
        "abc"
    };

    assert(strcmp("abc", longestCommonPrefix(strs, 2)) == 0);

    return 0;
}
