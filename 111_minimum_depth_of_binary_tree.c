#include <stdlib.h>
#include <assert.h>

#define min(A,B) ((A)<(B)?(A):(B))

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

int minDepth(struct TreeNode* root) {
    if(root == NULL)
        return 0;
    if(root->left == NULL)
        return minDepth(root->right)+1;
    if(root->right == NULL)
        return minDepth(root->left)+1;

    int lDepth = minDepth(root->left);
    int rDepth = minDepth(root->right);
    return min(lDepth, rDepth)+1;
}

int main() {
    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode*));
    root->val = 1;
    struct TreeNode* left = (struct TreeNode*)malloc(sizeof(struct TreeNode*));
    left->val = 2;
    root->left = left;
    root->right = NULL;
    left->left = NULL;
    left->right = NULL;

    assert(minDepth(root) == 2);

    return 0;
}
