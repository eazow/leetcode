#include <assert.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

int hasPathSum(struct TreeNode* root, int sum) {
    if(root == NULL)
        return 0;
    else if(root->left==NULL && root->right==NULL)
        return sum==root->val;

    return hasPathSum(root->left, sum-root->val) || 
        hasPathSum(root->right, sum-root->val);
}

int main() {
    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    root->val = 1;
    struct TreeNode* node1_1 = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node1_1->val = 5;
    root->left = node1_1;
    root->right = NULL;
    struct TreeNode* node2_1 = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node2_1->val = 6;
    node1_1->left = node2_1;
    node1_1->right = NULL;
    node2_1->left = NULL;
    node2_1->right = NULL;

    assert(hasPathSum(root, 12) == 1);
    assert(hasPathSum(root, 10) == 0);

    assert(hasPathSum(NULL, 0) == 0);

    return 0;
}
