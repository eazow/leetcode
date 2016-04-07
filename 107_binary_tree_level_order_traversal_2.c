#include <assert.h>
#include <stdlib.h>
#include <stdint.h>

#define SIZE 1000

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

typedef struct {
    struct TreeNode **base;
    int top;
    int size;
} Stack;

typedef struct Queue {
    Stack *stack1;
    Stack *stack2;
} Queue;

Stack *stack_create() {
    Stack *stack = (Stack *)malloc(sizeof(Stack));
    if(!stack) 
        return NULL;
    stack->base = (struct TreeNode **)malloc(sizeof(struct TreeNode *) * SIZE);
    stack->top = 0;
    stack->size = SIZE;
    return stack;
}

void stack_destroy(Stack *stack) {
    free(stack->base);
    free(stack);
}

int stack_enlarge(Stack *stack) {
    struct TreeNode **nodes = (struct TreeNode **)realloc(stack->base, sizeof(struct TreeNode *)*(stack->size+SIZE));
    if(nodes == NULL) 
        return 0;
    stack->base = nodes;
    stack->size += SIZE;
    return 1;
}

void stack_push(Stack *stack, struct TreeNode *node) {
    if(stack->top >= stack->size)
        stack_enlarge(stack);
    stack->base[stack->top++] = node;
}

struct TreeNode *stack_pop(Stack *stack) {
    if(stack->top == 0)
        return NULL;
    return stack->base[--stack->top];
}

int stack_empty(Stack *stack) {
    return stack->top==0;
}

int stack_size(Stack *stack) {
    return stack->top;
}

Queue *queue_create() {
    Queue *queue = (Queue *)malloc(sizeof(Queue));
    queue->stack1 = stack_create();
    queue->stack2 = stack_create();
    return queue;
}

void queue_push(Queue *queue, struct TreeNode *node) {
    stack_push(queue->stack1, node);
}

struct TreeNode *queue_pop(Queue *queue) {
    if(stack_empty(queue->stack2)) {
        while(!stack_empty(queue->stack1)) {
            struct TreeNode *node = stack_pop(queue->stack1);
            stack_push(queue->stack2, node);
        }
    }
    return stack_pop(queue->stack2);
}

int queue_empty(Queue *queue) {
    return stack_empty(queue->stack1) && stack_empty(queue->stack2);
}

int queue_size(Queue *queue) {
    return queue->stack1->top+queue->stack2->top;
}

void queue_destroy(Queue *queue) {
    free(queue->stack1->base);
    free(queue->stack1);
    free(queue->stack2->base);
    free(queue->stack2);
}

int **levelOrderBottom(struct TreeNode *root, int **columnSizes, int *returnSize) {
    if(root == NULL) {
        *returnSize = 0;
        *columnSizes = NULL;
        return NULL;
    }


    Queue *queue = queue_create();
    Stack *vals_stack = stack_create();
    Stack *nodes_count_stack = stack_create();
    int nodes_count = 0;
    int i = 0;
    queue_push(queue, root);
    struct TreeNode *tree_node = NULL;
    while(!queue_empty(queue)) {
        nodes_count = queue_size(queue);
        stack_push(nodes_count_stack, (struct TreeNode *)(intptr_t)nodes_count);
        
        for(i = 0; i < nodes_count; i++) {
            tree_node = queue_pop(queue);
            if(tree_node->left)
                queue_push(queue, tree_node->left);
            if(tree_node->right)
                queue_push(queue, tree_node->right);
            stack_push(vals_stack, (struct TreeNode *)(intptr_t)tree_node->val);
        }
    }

    int j = 0;
    *returnSize = stack_size(nodes_count_stack);
    *columnSizes = (int *)malloc(sizeof(int) * (*returnSize));
    int **return_arrays = (int **)malloc(sizeof(int *) * (*returnSize));


    while(!stack_empty(nodes_count_stack)) {
        nodes_count = (int)(intptr_t)stack_pop(nodes_count_stack);
        *(*columnSizes+j) =  nodes_count;
        int *nums = (int *)malloc(sizeof(int) * nodes_count);
        for(i = nodes_count-1; i >= 0; i--) {
            nums[i] = (int)(intptr_t)stack_pop(vals_stack);
        }
        return_arrays[j] = nums;
        j++;
    }

    stack_destroy(nodes_count_stack);
    stack_destroy(vals_stack);
    queue_destroy(queue);

    return return_arrays;
}

int main() {
    struct TreeNode *root = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    root->val = 1;
    struct TreeNode *node1_1 = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    node1_1->val = 2;
    struct TreeNode *node1_2 = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    node1_2->val = 3;
    root->left = node1_1;
    root->right = node1_2;
    node1_1->left = NULL;
    node1_1->right = NULL;
    node1_2->left = NULL;
    node1_2->right = NULL;

    int returnSize = 0;
    int *columnSizes = (int *)malloc(sizeof(int));
    int **return_array = levelOrderBottom(root, &columnSizes, &returnSize);

    assert(returnSize == 2);
    assert(return_array[0][0] = 1);
    assert(return_array[1][0] = 2);
    assert(return_array[1][1] = 3);

    return 0;
}
