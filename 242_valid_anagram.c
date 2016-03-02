#include <string.h>
#include <assert.h>

int isAnagram(char *s, char *t) {
    if(strlen(s) != strlen(t)) {
        return 0;
    }

    int statistics[26] = {0};
    int i = 0;
    for(i = 0; i < strlen(s); i++) {
        statistics[*(s+i)-'a']++;
        statistics[*(t+i)-'a']--;
    }
    
    for(i = 0; i < 26; i++) {
        if(statistics[i] != 0) {
            return 0;
        }
    }
    return 1;
}

int main(int argc, char *argv[]) {
    char s[100] = "anagram";
    char t[100] = "nagaram";

    assert(isAnagram(s, t) == 1);
    return 0;
}
