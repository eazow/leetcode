#include <assert.h>
#include <stdlib.h>
#include <stdio.h>

#define max(A,B) ((A)>(B)?(A):(B))

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

int height(struct TreeNode *root) {
    if(root == NULL)
        return 0;
    
    int left_height = height(root->left);
    if(left_height == -1)
        return -1;
    int right_height = height(root->right);
    if(right_height == -1)
        return -1;
    if(abs(left_height-right_height) > 1)
        return -1;

    return max(left_height, right_height)+1;
}

int isBalanced(struct TreeNode *root) {
    if(root == NULL)
        return 1;
    return height(root) >= 0;
}

int main() {
    struct TreeNode *root = malloc(sizeof(struct TreeNode));
    root->val = 5;

    struct TreeNode *left1_1 = malloc(sizeof(struct TreeNode));
    left1_1->val = 3;

    struct TreeNode *left2_1 = malloc(sizeof(struct TreeNode));
    left2_1->val = 1;

    root->left = left1_1;
    root->right = NULL;
    left1_1->left = left2_1;
    left1_1->right = NULL;
    left2_1->left = NULL;
    left2_1->right = NULL;

    assert(isBalanced(root) == 0);

    return 0;
}
