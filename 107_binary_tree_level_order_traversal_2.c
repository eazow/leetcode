#include <assert.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct Queue {
    struct TreeNode **node;
    int head;
    int tail;

}

int **levelOrderBottom(struct TreeNode *root, int **columnSizes, int *returnSize) {

}

void traversal(root) {
    Queue *queue = malloc(sizeof(Queue));
    if(root) {
        Queue->push(root);
        Queue->pop(root);
        
        if(root->left) {
            queue->push(root->left);
            queue->push(root->right);   
        }
    }

}

int main() {

    return 0;
}
