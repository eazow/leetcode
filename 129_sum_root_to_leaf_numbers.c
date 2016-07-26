#include <assert.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

int sumRecursively(struct TreeNode* node, int sum) {
    if(node == NULL)
        return sum;
    sum = sum*10+node->val;
    if(node->left==NULL && node->right==NULL) {
        return sum;
    }
    if(node->left && node->right==NULL) {
        sum = sumRecursively(node->left, sum);
    }
    else if(node->left==NULL && node->right!=NULL) {
        sum = sumRecursively(node->right, sum);
    }
    else {
        sum = sumRecursively(node->left, sum)+sumRecursively(node->right, sum);
    }

    return sum;
}

int sumNumbers(struct TreeNode* root) {
    return sumRecursively(root, 0);
}

int main() {
    struct TreeNode* root = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    root->val = 1;
    struct TreeNode* node1_1 = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    node1_1->val = 2;
    struct TreeNode* node1_2 = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    node1_2->val = 3;
    root->left = node1_1;
    root->right = node1_2;
    node1_1->left = NULL;
    node1_1->right = NULL;
    node1_2->left = NULL;
    node1_2->right = NULL;

    assert(sumNumbers(root) == 25);

    return 0;
}
