#include <assert.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* preorderTraversal(struct TreeNode* root, int* returnSize) {
    if(root == NULL)
        return NULL;

    int *vals = (int *)malloc(sizeof(int) * 1000);
    int valsTop = 0;
    struct TreeNode* node = root;
    struct TreeNode** nodes = (struct TreeNode **)malloc(sizeof(struct TreeNode *) * 1000);
    int nodesTop = 0;
    nodes[nodesTop++] = root;

    while(nodesTop > 0) {
        node = nodes[--nodesTop];
        vals[valsTop++] = node->val;

        if(node->right)
            nodes[nodesTop++] = node->right;
        if(node->left)
            nodes[nodesTop++] = node->left;
    }
    *returnSize = valsTop;
    return vals;
}

int main() {
    struct TreeNode* root = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    root->val = 1;
    struct TreeNode* node1_2 = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    node1_2->val = 2;
    root->left = NULL;
    root->right = node1_2;
    struct TreeNode* node2_3 = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    node2_3->val = 3;
    node1_2->left = node2_3;
    node1_2->right = NULL;
    node2_3->left = NULL;
    node2_3->right = NULL;

    int returnSize = 0;
    int* vals = preorderTraversal(root, &returnSize);
    assert(returnSize == 3);
    assert(vals[0] == 1);
    assert(vals[1] == 2);
    assert(vals[2] == 3);

    return 0;
}
