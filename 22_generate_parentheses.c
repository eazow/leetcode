#include <assert.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

#define SIZE 200

void addParenthesisRecursively(int left, int right, char* str, char**result, int* returnSize, int n) {
    if((left == 0) && (right == 0))
        result[(*returnSize)++] = str;
    else {
        char* newStr = (char *)malloc(sizeof(char) * (2*n+1));
        if(left > 0) {
            strcpy(newStr, str);
            addParenthesisRecursively(left-1, right+1, strcat(newStr, "("), result, returnSize, n);
        }
        if(right > 0) {
            strcpy(newStr, str);
            addParenthesisRecursively(left, right-1, strcat(newStr, ")"), result, returnSize, n);
       }
    }
}

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** generateParenthesis(int n, int* returnSize) {
    char** result = (char **)malloc(sizeof(char *) * SIZE);
    addParenthesisRecursively(n, 0, "", result, returnSize, n);
    return result;
}

int main() {
    int returnSize = 0;
    char** result = generateParenthesis(3, &returnSize);
    printf("%s\n", result[0]);
    printf("%s\n", result[1]);
    assert(returnSize == 2);

    return 0;
}
