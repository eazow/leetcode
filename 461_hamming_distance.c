#include <assert.h>
#include <stdio.h>

int hammingDistance(int x, int y) {
    int result = x^y;
    int distance = 0;

    while(result > 0) {
        if(result&1)
	    distance++;
	
	result >>= 1;
	printf("%d\n", result);
    }

    return distance;
}

int main() {
    assert(hammingDistance(1,4) == 2);

    return 0;
}
