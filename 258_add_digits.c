#include <assert.h>

int addDigits(int num) {
	long step = 10;
	int sum = num%step;

	while(num/step>=1) {
		num = num/step;
		sum += num%10;
	}
	if(sum >= 10) {
		return addDigits(sum);
	}
	return sum;
}

int main(int argc, char *arg[]) {
	assert(addDigits(38) == 2);
	assert(addDigits(100) == 1);
	assert(addDigits(2032610959) == 1);
}
