#include <stdlib.h>

typedef struct {
    int *base;
    int head;
    int tail;
    int size;
} Queue;

typedef struct {
    Queue *queue1;
    Queue *queue2;
} Stack;

Queue *queueCreate(int maxSize) {
    Queue *queue = (Queue *)malloc(sizeof(Queue));
    queue->base = (int *)malloc(sizeof(int));
    queue->size = maxSize;
    queue->head = 0;
    queue->tail = 0;
    return queue;
}
/* Create a stack */
void stackCreate(Stack *stack, int maxSize) {
    
}

/* Push element x onto stack */
void stackPush(Stack *stack, int element) {

}

/* Removes the element on top of the stack */
void stackPop(Stack *stack) {

}

/* Get the top element */
int stackTop(Stack *stack) {

}

/* Return whether the stack is empty */
int stackEmpty(Stack *stack) {

}

/* Destroy the stack */
void stackDestroy(Stack *stack) {

}
