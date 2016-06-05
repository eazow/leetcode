#include <assert.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* inorderTraversal(struct TreeNode* root, int* returnSize) {
    struct TreeNode* node;
    struct TreeNode** nodes = (struct TreeNode **)malloc(sizeof(struct TreeNode *) * 1000);
    node = root;
    int nodesTop = 0;
    int* vals = (int *)malloc(sizeof(int) * 1000);
    int valsTop = 0;
    while(node!=NULL || nodesTop!=0) {
        while(node != NULL) {
            nodes[nodesTop++] = node;
            node = node->left;
        }
        node = nodes[--nodesTop];
        vals[valsTop++] = node->val;
        node = node->right;
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
    int* vals = inorderTraversal(root, &returnSize);
    assert(returnSize == 3);
    return 0;
}
