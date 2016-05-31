#include <assert.h>

int maxProfit(int* prices, int pricesSize) {
    int i = 0;
    int profit = 0;
    for(i = 0; i < pricesSize-1; i++) {
        if(prices[i+1] > prices[i])
            profit += prices[i+1]-prices[i];
    }
    return profit;
}

int main() {
    int prices[5] = {1,5,3,9,2};
    assert(maxProfit(prices, 5) == 10);

    return 0;
}
