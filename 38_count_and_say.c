#include <assert.h>
#include <string.h>

char* countAndSay(int n) {
    if(n == 1)
        return "1";
    char *s = "1";
    int i = 0;
    int strLen = strlen(s);
    int count = 0;
    char pre = s[0];
    char cur;
    char* statistic = (char*)malloc(sizeof(char) * (2 * strlen + 2));
    while(++s) {
        cur = s;
        if(cur == pre)
            count++;
        else {
            pre = *s;
        }
    }

}

int main() {
    assert(countAndSay(1) == "1");

    return 0;
}
