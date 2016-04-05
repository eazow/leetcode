#include <assert.h>
#include <stdlib.h>

#define MAX_SIZE 1000

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
    stack *stack2;
} Queue;

int **levelOrderBottom(struct TreeNode *root, int **columnSizes, int *returnSize) {
    Queue *queue = queue_create();
    Stack *vals_stack = stack_create();
    Stack *nodes_count_stack = stack_create();
    int queue_size = 0;
    if(root) {
        queue_push(queue, root);
        int i = 0;
        struct TreeNode *tree_node = NULL;
        while(!queue_empty(queue)) {
            queue_size = queue_size(queue);
            stack_push(nodes_count_stack, (struct TreeNode *)queue_size);

            tree_node = queue_pop(queue);
            for(i = 0; i < queue_size; i++) {
                if(tree_node->left)
                    queue_push(queue, tree_node->left);
                if(tree_node->right)
                    queue_push(queue, tree_node->right);
            }
            stack_push(vals_stack, (struct TreeNode *)tree_node->val);
        }
    }

    int nodes_count = 0;
    int j = 0;
    *returnSize = stack_size(nodes_count_stack);
    *columnSizes = (int *)malloc(sizeof(int) * (*returnSize));
    while(!stack_empty(nodes_count_stack)) {
        j = 0;
        nodes_count = stack_pop(nodes_count_stack);
        *(*columnSizes+j) =  nodes_count;
        for(i = 0; i < nodes_count; i++) {
            *((*columnSizes+j)+i) = stack_pop(vals_stack);
        }
        j++;
    }

}

int main() {

    return 0;
}
