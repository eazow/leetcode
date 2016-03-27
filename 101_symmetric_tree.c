#include <assert.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

int isAMirror(struct TreeNode *left, struct TreeNode *right) {
    if(left==NULL && right==NULL)
        return 1;
    if(left==NULL || right==NULL)
        return 0;

    return (left->val == right->val) && isAMirror(left->left, right->right) && isAMirror(left->right, right->left);
}

int isSymmetric(struct TreeNode *root) {
    if(root == NULL)
        return 1;

    return isAMirror(root->left, root->right);
}

int main() {
    struct TreeNode *root = malloc(sizeof(struct TreeNode));
    root->val = 1;

    struct TreeNode *left = malloc(sizeof(struct TreeNode));
    left->val = 2;

    struct TreeNode *right = malloc(sizeof(struct TreeNode));
    right->val = 3;

    root->left = left;
    root->right = right;
    left->left = NULL;
    left->right = NULL;
    right->left = NULL;
    right->right = NULL;

    assert(isSymmetric(root) == 0);

    return 0;
}
