#include <assert.h>
#include <stdlib.h>

#define max(A, B) ((A)>(B)?(A):(B))

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

int* robRecursively(struct TreeNode* node) {
    if(node == NULL)
        return (int *)calloc(2, sizeof(int));
    int* left = robRecursively(node->left);
    int* right = robRecursively(node->right);
    int* result = (int *)calloc(2, sizeof(int));
    result[0] = node->val+left[1]+right[1];
    result[1] = max(left[0]+right[0], left[1]+right[1]);
    return result;
}

int rob(struct TreeNode* root) {
    int* result = robRecursively(root);
    return max(result[0], result[1]);
}

int main() {
    struct TreeNode* root = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    root->val = 5;
    struct TreeNode* left = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    left->val = 1;
    struct TreeNode* right = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    right->val = 2;
    root->left = left;
    root->right = right;
    left->left = NULL;
    left->right = NULL;
    right->left = NULL;
    right->right = NULL;

    assert(rob(root) == 5);

    return 0;
}
