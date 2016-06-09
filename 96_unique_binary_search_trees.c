#include <assert.h>
#include <stdlib.h>

int numTrees(int n) {
    int* numTrees = (int *)malloc(sizeof(int) * (n+1));
    if(n = 1)
        numTrees[n] = 1;
    int i = 0;
    int j = 0;
    for(i = 1; i <= n; i++) {
        for(j = 1; j < i; j++)
            numTrees[i] = numTrees[j]+numTrees[i-j];
    }

}
