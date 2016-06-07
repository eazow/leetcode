#include <assert.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct List {
    int* vals;
    int size;
    int top;
};

void inorderTraversal(struct TreeNode* node, struct List* list) {
    if(node->left != NULL)
        inorderTraversal(node->left, list);
    list->vals[list->top++] = node->val;
    if(node->right != NULL)
        inorderTraversal(node->right, list);
}

int kthSmallest(struct TreeNode* root, int k) {
    struct List* list = (struct List *)malloc(sizeof(struct List));
    int size = 10000;
    list->vals = (int *)malloc(sizeof(int) * size);
    list->size = size;
    list->top = 0;
    inorderTraversal(root, list);
    return list->vals[k-1];
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
