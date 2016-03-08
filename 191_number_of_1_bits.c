#include <assert.h>

int hammingWeight(int n) {
    int i = 0, count = 0;

    for(i = 0; i < 32; i++) {
        if(n>>i & 1)
            count++;
    }

    return count;
}

int main(int argc, char *argv[]) {
    int n = 010011;
    assert(hammingWeight(n)==3);
}
