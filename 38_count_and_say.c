#include <assert.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

char* countAndSay(int n) {
    if(n == 1)
        return "1";

    int nIndex = 1;
    char *s = "1";
    char *statistic;
    for(; nIndex < n; nIndex++) {
        int i = 0;
        int strLen = strlen(s);
        int count = 0;
        char pre = s[0];
        char cur;
        statistic = (char*)malloc(sizeof(char) * (2 * strLen + 2));
        int j = 0;
        for(i = 0; i < strLen; i++) {
            cur = s[i];
            if(cur == pre)
                count++;
            else {
                statistic[j++] = '0' + count;
                statistic[j++] = pre;
                pre = s[i];
                count = 1;
            }
        }
        if(count > 0) {
            statistic[j++] = '0' + count;
            statistic[j++] = cur;
        }
        statistic[j] = '\0';
        s = statistic;
    }
    return statistic;
}

int main() {
    assert(countAndSay(1) == "1");
    assert(strcmp(countAndSay(2),"11")==0);
    assert(strcmp(countAndSay(10), "13211311123113112211")==0);

    return 0;
}
