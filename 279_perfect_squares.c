#include <assert.h>
#include <stdlib.h>
#include <limits.h>

int numSquares(int n) {
    int* squares = (int *)malloc(sizeof(int) * (n+1));
    squares[0] = 0;
    int i = 0, j = 0;
    int min = INT_MAX;
    int num = 0;
    for(i = 1; i <=n; i++)
        squares[i] = INT_MAX;
    for(i = 1; i <= n; i++) {
        min = INT_MAX;
        for(j = 1; j*j <= i; j++) {
            num = 1+squares[i-j*j];
            min = num<min?num:min;
        }
        squares[i] = min;
    }
    return squares[n];
}

int main() {
    assert(numSquares(10) == 2);
    assert(numSquares(56) == 3);

    return 0;
}
