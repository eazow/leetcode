#include <assert.h>
#include <stdlib.h>

int numTrees(int n) {
    int* numTrees = (int *)calloc(n+1, sizeof(int));
    numTrees[0] = 1;
    int i = 0;
    int j = 0;
    for(i = 1; i <= n; i++)
        for(j = 0; j < i; j++)
            numTrees[i] += numTrees[j]*numTrees[i-j-1];

    return numTrees[n];
}

int main() {
    assert(numTrees(3) == 5);

    return 0;
}
