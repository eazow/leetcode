#include <string.h>
#include <assert.h>

/*
 * I=1 V=5 X=10 L=50 C=100 D=500 M=1000
 */
int romanToInt(char *s) {
    int map[26] = {0};
    map['I'-'A'] = 1;
    map['V'-'A'] = 5;
    map['X'-'A'] = 10;
    map['L'-'A'] = 50;
    map['C'-'A'] = 100;
    map['D'-'A'] = 500;
    map['M'-'A'] = 1000;

    int i = 0, sum = 0;
    for(i = 0; i < strlen(s); i++) {
        if(i+1 < strlen(s) && map[*(s+i)-'A']<map[*(s+i+1)-'A'])
            sum -= map[*(s+i)-'A'];
        else 
            sum += map[*(s+i)-'A'];
    }
    return sum;
}

int main(int argc, char *argv[]) {
    assert(romanToInt("I")==1);
    assert(romanToInt("IV")==4);
}
