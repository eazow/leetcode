#include <assert.h>
#include <string.h>

int wordPattern(char* pattern, char* str) {
    int patternLen = strlen(pattern);
    int strLen = strlen(str);

    int i, j;
    char patternChar;
    char strChar;
    int hash = 0;
    int map[26] = {0};
    for(i=0,j=0; i < patternLen; i++) {
        hash = 0;
        patternChar = pattern[i];
        while(((strChar=str[j]) != ' ') && (j < strLen)) {
            hash = hash*26 + (strChar-'a'+1);
            j++;
        }
        if(strChar == ' ')
            j++;
        if(map[patternChar-'a'] == 0) {
            map[patternChar-'a'] = hash;
            int mapIndex = 0;
            while(mapIndex < 26) {
                if(mapIndex!=(patternChar-'a') && map[mapIndex]==hash)
                    return 0;
                mapIndex++;
            }
        }
        else if(map[patternChar-'a'] != hash)
            return 0;
    }

    return i==patternLen&&j==strLen;
}

int main() {
    assert(wordPattern("abba", "dog cat cat dog") == 1);
    assert(wordPattern("abba", "dog cat cat fish") == 0);
    assert(wordPattern("aaaa", "dog cat cat dog") == 0);
    assert(wordPattern("abba", "dog dog dog dog") == 0);
    
    return 0;
}
