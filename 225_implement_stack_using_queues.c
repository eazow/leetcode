#include <stdlib.h>
#include <assert.h>

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

int queueSize(Queue *queue) {
    return queue->tail-queue->head;
}

void queuePush(Queue *queue, int element) {
    queue->base[queue->tail++] = element;
}

int queuePop(Queue *queue) {
    return queue->base[queue->head++];
}

void queueDestroy(Queue *queue) {
    free(queue->base);
    free(queue);
}

/* Create a stack */
void stackCreate(Stack *stack, int maxSize) {
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
    else if(queueEmpty(stack->queue1)) {
        while(queueSize(stack->queue2) > 1) {
            queuePush(stack->queue1, queuePop(stack->queue2));
        }
        queuePop(stack->queue2);
    }
}

/* Get the top element */
int stackTop(Stack *stack) {
    if(queueEmpty(stack->queue1) && queueEmpty(stack->queue2))
        return 0;
    if(queueEmpty(stack->queue2)) {
        while(queueSize(stack->queue1) > 1) {
            queuePush(stack->queue2, queuePop(stack->queue1));
        }
        int element = queuePop(stack->queue1);
        queuePush(stack->queue2, element);
        return element;
    }
    else {
        while(queueSize(stack->queue2) > 1) {
            queuePush(stack->queue1, queuePop(stack->queue2));    
        }
        int element = queuePop(stack->queue2);
        queuePush(stack->queue1, element);
        return element;
    }
}

/* Return whether the stack is empty */
int stackEmpty(Stack *stack) {
    return queueEmpty(stack->queue1) && queueEmpty(stack->queue2);
}

int stackSize(Stack *stack) {
    int queueSize1 = queueSize(stack->queue1);
    int queueSize2 = queueSize(stack->queue2);
    return queueSize1>queueSize2?queueSize1:queueSize2;
}

/* Destroy the stack */
void stackDestroy(Stack *stack) {
    queueDestroy(stack->queue1);
    queueDestroy(stack->queue2);
}

int main() {
    Stack *stack = (Stack *)malloc(sizeof(Stack));
    stackCreate(stack, 100);

    assert(stackEmpty(stack) == 1);
    stackPush(stack, 1);
    assert(stackSize(stack) == 1);
    assert(stackEmpty(stack) == 0);
    assert(stackTop(stack) == 1);
    stackPop(stack);
    assert(stackEmpty(stack) == 1);

    free(stack);
    return 0;
}
