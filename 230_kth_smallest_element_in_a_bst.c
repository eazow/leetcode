#include <assert.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct Stack {
    int* vals;
    int size;
    int top;
};

void inorderTraversal(struct TreeNode* node, struct Stack* stack) {
    if(node->left != NULL)
        inorderTraversal(node->left, stack);
    stack->vals[stack->top++] = node->val;
    if(node->right != NULL)
        inorderTraversal(node->left, stack);
}

int kthSmallest(struct TreeNode* root, int k) {
    struct Stack* stack = (struct Stack *)malloc(sizeof(struct Stack));
    int size = 1000;
    stack->vals = (int *)malloc(sizeof(int) * size);
    stack->size = size;
    stack->top = 0;
    inorderTraversal(root, stack);
    return stack->vals[k-1];
}

int main() {
    struct TreeNode* root = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    root->val = 2;
    struct TreeNode* left = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    left->val = 1;
    struct TreeNode* right = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    right->val = 3;
    root->left = left;
    root->right = right;
    left->left = NULL;
    left->right = NULL;
    right->left = NULL;
    right->right = NULL;
    assert(kthSmallest(root, 2) == 2);

    return 0;
}
