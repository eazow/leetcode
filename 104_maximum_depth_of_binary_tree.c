#include <stdlib.h>
#include <assert.h>

typedef struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
}TreeNode;

int maxDepth(struct TreeNode *root) {
    if(root == NULL) {
        return 0;
    }
    int leftDepth = 1, rightDepth = 1;
    leftDepth = maxDepth(root->left)+1;
    rightDepth = maxDepth(root->right)+1;
    return leftDepth>rightDepth?leftDepth:rightDepth;
}

int main(int argc, char *argv[]) {
    TreeNode *root = malloc(sizeof(TreeNode));
    root->val = 1;
    root->left = NULL;
    root->right = NULL;

    TreeNode *leftNode = malloc(sizeof(TreeNode));
    leftNode->val = 2;
    leftNode->left = NULL;
    leftNode->right = NULL;
    root->left = leftNode;

    assert(maxDepth(NULL) == 0);
    assert(maxDepth(root) == 2);

    return 0;
}
