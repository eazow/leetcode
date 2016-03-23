#include <assert.h>
#include <stdlib.h>
#include <stdio.h>

typedef struct {
    int *stack;
    int *stack2;
    int top;
    int top2;
} Queue;

/* Create a queue */
void queueCreate(Queue *queue, int maxSize) {
    queue->stack = (int *)malloc(sizeof(int)*maxSize);
    queue->stack2 = (int *)malloc(sizeof(int)*maxSize);
    queue->top = 0;
    queue->top2 = 0;
}

/* Push element x to the back of queue */
void queuePush(Queue *queue, int element) {
    queue->stack[queue->top++] = element;
}

/* Remove the element from front of queue */
void queuePop(Queue *queue) {
    while(queue->top > 0)
        *(queue->stack2+queue->top2++) = *(queue->stack+(--queue->top));
    queue->top2--;
    while(queue->top2 > 0)
        *(queue->stack+queue->top++) = *(queue->stack2+(--queue->top2));
}

/* Get the front element */
int queuePeek(Queue *queue) {
    int result = 0;
    while(queue->top > 0)
        *(queue->stack2+queue->top2++) = *(queue->stack+(--queue->top));
    if(queue->top2 > 0)
        result = *(queue->stack2+queue->top2-1);
    while(queue->top2 > 0)
        *(queue->stack+queue->top++) = *(queue->stack2+(--queue->top2));
    return result;
}

/* Return whether the queue is empty */
int queueEmpty(Queue *queue) {
    return queue->top==0;
}

/* Destroy the queue */
void queueDestroy(Queue *queue) {
    free(queue->stack);
    free(queue->stack2);
}

int main() {
    Queue *queue = malloc(sizeof(Queue));
    queueCreate(queue, 10);
    queuePush(queue, 1);
    queuePush(queue, 2);
    queuePush(queue, 3);
    queuePop(queue);
    queuePop(queue);
    assert(queuePeek(queue) == 3);
    assert(queueEmpty(queue) == 0);
    queueDestroy(queue);

    return 0;
}

