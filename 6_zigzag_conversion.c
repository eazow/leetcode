#include <assert.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

char* convert(char* s, int numRows) {
    int len = strlen(s);
    char *statistics = (char *)malloc(sizeof(char)*len*numRows);
    int i = 0;
    for(i = 0; i < len*numRows; i++) {
        statistics[i] = '-';
    }

    int row, col;
    int oddCol = 1;
    int assendOrder = 0;
    int sI = 0;
    for(col = 0; col < len; col++) {
        //even column
        if(col%2==0) {
            if(assendOrder == 0) {
                row = 0;
                while(row < numRows) {
                    statistics[(row++)*len+col] = s[sI++];
                }
                assendOrder = 1;
            }
            else {
                row = numRows-1;
                while(row >= 0) {
                    statistics[(row--)*len+col] = s[sI++];
                }
                assendOrder = 0;
            }
        }
        //odd column
        else {
            if(assendOrder == 0) {
                row = 1;
                while(row < numRows-1) {
                    statistics[(row++)*len+col] = s[sI++];
                }
                assendOrder = 1;
            }
            else {
                row = numRows-2;
                while(row >= 1) {
                    statistics[(row--)*len+col] = s[sI++];
                }
                assendOrder = 0;
            }
        }
    }
    for(i = 0; i < len*numRows; i++)
        printf("%c", statistics[i]);

    return statistics;
}

int main() {
    convert("PAYPALISHIRING", 3);

    return 0;
}
