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
    queue->base = (int *)malloc(sizeof(int)*(maxSize+1));
    queue->size = maxSize;
    queue->head = 0;
    queue->tail = 0;
    return queue;
}

int queueEmpty(Queue *queue) {
    return queue->head == queue->tail;
}

void queueEnlarge(Queue *queue) {
}

int queueSize(Queue *queue) {
    return queue->tail-queue->head;
}

void queuePush(Queue *queue, int element) {
    if(queue->tail>=queue->size)
        queueEnlarge(queue);
    queue->base[queue->tail++] = element;
}

int queuePop(Queue *queue) {
    if(queueEmpty(queue))
        return 0;
    return queue->base[queue->head++];
}

/* Create a stack */
void stackCreate(Stack *stack, int maxSize) {
   stack = (Stack *)malloc(sizeof(Stack));
   stack->queue1 = queueCreate(maxSize);
   stack->queue2 = queueCreate(maxSize);
}

/* Push element x onto stack */
void stackPush(Stack *stack, int element) {
    if(queueEmpty(stack->queue2))
        queuePush(stack->queue1, element);
    else
        queuePush(stack->queue2, element);
}

/* Removes the element on top of the stack */
void stackPop(Stack *stack) {
    if(queueEmpty(stack->queue2)) {
        while(queueSize(stack->queue1) > 1) {
            int element = queuePop(stack->queue1);
            queuePush(stack->queue2, element);
        }
        queuePop(stack->queue1);
    }
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
