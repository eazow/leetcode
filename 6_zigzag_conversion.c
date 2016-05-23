#include <assert.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

char* filter(char* s, int len) {
    int i = 0;
    char* str = (char *)malloc(sizeof(char)*(len+1));
    int strI = 0;
    for(i = 0; strI < len; i++) {
        if(s[i] != '#')
            str[strI++] = s[i];  
    }
    str[strI] = '\0';
    return str;
}

char* convert(char* s, int numRows) {
    int len = strlen(s);
    char *statistics = (char *)malloc(sizeof(char)*len*numRows);
    int i = 0;
    for(i = 0; i < len*numRows; i++) {
        statistics[i] = '#';
    }

    int row, col;
    int oddCol = 1;
    int assendOrder = 0;
    int sI = 0;
    for(col = 0; col < len && sI < len; col++) {
        //even column
        if(col%2==0) {
            if(assendOrder == 0) {
                row = 0;
                while(row < numRows && sI < len)
                    statistics[(row++)*len+col] = s[sI++];
            }
            else {
                row = numRows-1;
                while(row >= 0 && sI < len)
                    statistics[(row--)*len+col] = s[sI++];
                assendOrder = 0;
            }
        }
        //odd column
        else {
            if(assendOrder == 0) {
                row = 1;
                while(row < numRows-1 && sI < len)
                    statistics[(row++)*len+col] = s[sI++];
                assendOrder = 1;
            }
            else {
                row = numRows-2;
                while(row >= 1 && sI < len)
                    statistics[(row--)*len+col] = s[sI++];
                assendOrder = 0;
            }
        }
    }

    return filter(statistics, len);
}

int main() {
    printf("%s\n", convert("PAYPALISHIRING", 3));

    return 0;
}
