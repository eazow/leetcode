#include <assert.h>
#include <stdlib.h>
#include <string.h>

typedef struct Stack {
    int *base;
    int top;
    int size;
}Stack;

void push(Stack* stack, int e) {
    stack->base[stack->top++] = e;
}

int pop(Stack* stack) {
    return stack->base[--(stack->top)];
}

int empty(Stack* stack) {
    return stack->top==0;
}

Stack* createStack() {
    Stack* stack = (Stack*)malloc(sizeof(Stack));
    stack->base = (int *)malloc(sizeof(int)*1000);
    stack->size = 1000;
    stack->top = 0;
    return stack;
}

int isValid(char* s) {
    Stack* stack = createStack();
    int i = 0;
    int len = strlen(s);
    char c;
    for(i = 0; i < len; i++) {
        c = s[i];
        if(c=='{' || c=='(' || c=='[')
            push(stack, c);
        else if(c=='}' || c==')' || c==']') {
            if(empty(stack))
                return 0;
            char temp = pop(stack);
            if(temp-c > 2) 
                return 0;
        }
    }
    return empty(stack);
}

int main() {
    assert(isValid("((({{[[[]]]}})))") == 1);
    assert(isValid("({[}])") == 0);

    return 0;
}
