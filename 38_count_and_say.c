#include <assert.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

char* countAndSay(int n) {
    if(n == 1)
        return "1";
    char *s = "1";
    int i = 0;
    int strLen = strlen(s);
    int count = 0;
    char pre = s[0];
    char cur;
    char* statistic = (char*)malloc(sizeof(char) * (2 * strLen + 2));
    int j = 0;
    while(++s) {
        cur = *s;
        if(cur == pre)
            count++;
        else {
            pre = *s;
            statistic[j++] = '0' + count;
            statistic[j++] = '0' + pre;
        }
    }
    statistic[j] = '\0';

    return "1";
}

int main() {
    assert(countAndSay(1) == "1");

    countAndSay(2);

    return 0;
}
