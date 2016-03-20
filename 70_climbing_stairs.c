#include <assert.h>
#include <stdio.h>


/**
 * f(2) = f(0) + f(1)
 * f(3) = f(1) + f(2)
 * f(4) = f(2) + f(3) 
 * f(5) = f(3) + f(4)
 */
int climbStairs(int n) {
/*
	if(n < 3) 
		return n;
	return climbStairs(n-1) + climbStairs(n-2);
*/
	int pre1 = 0, pre2 = 1, result = 1;

	while(n-- > 0) {
		result = pre1 + pre2;
		pre1 = pre2;
		pre2 = result;
	}

	return result;
}

int main(int argc, char **argv) {
    assert(climbStairs(1) == 1);
    assert(climbStairs(2) == 2);
    assert(climbStairs(3) == 3);
	assert(climbStairs(4) == 5);
	assert(climbStairs(5) == 8);

    return 0;
}
