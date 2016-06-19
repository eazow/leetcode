#include <assert.h>
#include <stdlib.h>

#define max(A,B) ((A)>(B)?(A):(B))

int maxProfit(int* prices, int pricesSize) {
    int i = 0;
    int* buy = (int *)malloc(sizeof(int) * pricesSize);
    int* sell = (int *)malloc(sizeof(int) * pricesSize);
    buy[0] = -prices[0];
    buy[1] = -prices[1];
    sell[0] = 0;
    sell[1] = prices[1]-prices[0];
    sell[1] = sell[1]>0?sell[1]:0;

    for(i = 2; i < pricesSize; i++) {
        buy[i] = max(buy[i-1], sell[i-2]-prices[i]);
        sell[i] = max(buy[i-1]+prices[i], sell[i-1]);
    }
    return sell[i-1];
}

int main() {
    int nums[5] = {1,2,3,0,2};
    assert(maxProfit(nums, 5) == 3);

    return 0;
}
