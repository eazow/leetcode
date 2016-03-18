#include <assert.h>

int climbStairs(int n) {
    if(n<=3)
        return n;
    return climbStairs(n-1)+climbStairs(n-2);
}

int main(int argc, char **argv) {
    assert(climbStairs(1) == 1);
    assert(climbStairs(2) == 2);
    assert(climbStairs(3) == 3);

    climbStairs(50);


    return 0;
}
