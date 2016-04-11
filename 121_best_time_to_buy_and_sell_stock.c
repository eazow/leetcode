#include <assert.h>
#define min(A,B) ((A)<(B)?(A):(B))
#define max(A,B) ((A)>(B)?(A):(B))

int maxProfit(int *prices, int pricesSize) {
    int i = 0;
    int minPrice = pricesSize>0?prices[0]:0, maxProfit = 0;

    for(i = 0; i < pricesSize; i++) {
        minPrice = min(minPrice, prices[i]);
        maxProfit = max(maxProfit, prices[i]-minPrice);
    }
    
    return maxProfit;
}

int main() {
    int prices[6] = {1,2,3,4,5,6};
    assert(maxProfit(prices, 6) == 5);

    int prices2[2] = {2,1};
    assert(maxProfit(prices2, 2) == 0);

    return 0;
}
