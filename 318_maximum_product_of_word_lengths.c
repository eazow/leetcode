#include <assert.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int maxProduct(char** words, int wordsSize) {
    int i = 0;
    int j = 0;
    char *word = NULL;
    int* vals = (int *)malloc(sizeof(int) * wordsSize);
    for(i = 0; i < wordsSize; i++) {
        word = words[i];
        int wordLen = strlen(word);
        int val = 0;
        for(j = 0; j < wordLen; j++)
            val |= 1 << (word[j]-'a');
        vals[i] = val;
    }
    int product = 0;
    int maxProduct = 0;
    for(i = 0; i < wordsSize; i++) {
        for(j = 0; j < wordsSize; j++) {
            if((i != j) && ((vals[i]&vals[j])==0)) {
                product = strlen(words[i]) * strlen(words[j]);
                maxProduct = maxProduct>product?maxProduct:product;
            }
        }
    }
    return maxProduct;
}

int main() {
    char* words[6] = {"abcw", "baz", "foo", "bar", "xtfn", "abcdef"};
    assert(maxProduct(words, 6) == 16);

    return 0;
}
