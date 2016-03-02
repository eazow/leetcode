#include <stdlib.h>
#include <assert.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct TreeNode *invertTree(struct TreeNode *root) {
    if(root == NULL) {
        return NULL;
    }
    struct TreeNode *temp = root->left;
    root->left = root->right;
    root->right = temp;
    invertTree(root->left);
    invertTree(root->right);
    return root;
}

int main(int argc, char *argv[]) {
    struct TreeNode *root = malloc(sizeof(struct TreeNode));
    struct TreeNode *left = malloc(sizeof(struct TreeNode));
    struct TreeNode *right = malloc(sizeof(struct TreeNode));

    left->val = 2;
    right->val = 3;
    root->val = 1;
    root->left = left;
    root->right = right;

    root = invertTree(root);

    assert(root->left->val==3);
    assert(root->right->val==2);
    return 0;
}
