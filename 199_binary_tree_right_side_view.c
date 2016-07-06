#include <assert.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

#define SIZE 100

void rightSideViewRecursively(struct TreeNode* node, int level, int* vals, int* returnSize) {
    if(node == NULL)
        return;
    if(*returnSize == level)
        vals[(*returnSize)++] = node->val;

    rightSideViewRecursively(node->right, level+1, vals, returnSize);
    rightSideViewRecursively(node->left, level+1, vals, returnSize);
}

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* rightSideView(struct TreeNode* root, int* returnSize) {
    int* vals = (int *)malloc(sizeof(int) * SIZE);
    rightSideViewRecursively(root, 0, vals, returnSize);

    return vals;
}

int main() {
    struct TreeNode* root = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    root->val = 1;
    struct TreeNode* node1_1 = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    node1_1->val = 2;
    node1_1->left = NULL;
    node1_1->right = NULL;
    root->left = node1_1;
    struct TreeNode* node1_2 = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    node1_2->val = 3;
    node1_2->left = NULL;
    node1_2->right = NULL;
    root->right = node1_2;

    int returnSize = 0;
    int* vals = rightSideView(root, &returnSize);
    assert(vals[0] == 1);
    assert(vals[1] == 3);
    assert(returnSize == 2); 
}

