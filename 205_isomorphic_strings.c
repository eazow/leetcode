#include <assert.h>
#include <string.h>

int isIsomorphic(char* s, char* t) {
    int i =0;
    int len = strlen(s);
    char mapS[128] = {0};
    char mapT[128] = {0};
    
    char cS, cT;
    for(i = 0; i < len; i++) {
        cS = s[i];
        cT = t[i];
        if(mapS[cS] == 0 && mapT[cT] == 0) {
            mapS[cS] = cT;
            mapT[cT] = cS;
            continue;
        }
        if(mapS[cS] != cT)
            return 0;
    }

    return 1;
}

int main() {
    assert(isIsomorphic("egg", "add") == 1);
    assert(isIsomorphic("foo", "bar") == 0);
    assert(isIsomorphic("paper", "title") == 1);

    return 0;
}
