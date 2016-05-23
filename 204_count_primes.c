#include <assert.h>
#include <stdlib.h>

int countPrimes(int n) {
    //0 and 1 are not primes
    int count = n-1;
    int* isPrime = (int *)malloc(sizeof(int)*(n+1));
    int i = 0;
    for(i = 0; i <= n; i++) 
        isPrime[i] = 1;

    int j = 0;
    for(i = 2; i <= n; i++) {
        for(j = i; i*j <= n; j++) {
            if(isPrime[i*j]) {
                isPrime[i*j] = 0;     
                count--;
            }
        }
        
    }
    return count;
}

int main() {
    assert(countPrimes(10) == 4);

    countPrimes(499979);

    return 0;
}
