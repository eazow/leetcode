#include <assert.h>
#include <string.h>

int compareVersion(char* version1, char* version2) {
    int versionInt1, versionInt2;
    while(*version1!='\0' || *version2!='\0') {
        versionInt1 = 0;
        while(*version1 != '.' && *version1!='\0') {
            versionInt1 = versionInt1*10+*version1-'0';
            version1++;
        }
        if(*version1 == '.')
            version1++;
        versionInt2 = 0;
        while(*version2 != '.' && *version2!='\0') {
            versionInt2 = versionInt2*10+*version2-'0';
            version2++;
        }
        if(*version2 == '.')
            version2++;
        if(versionInt1 > versionInt2)
            return 1;
        else if(versionInt1 < versionInt2)
            return -1;
    }
    return 0;
}

int main() {
    assert(compareVersion("13.37", "13.37.2") == -1);

    return 0;
}
