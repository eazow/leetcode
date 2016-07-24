#include <assert.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

int sumRecursively(struct TreeNode* node, int sum) {
    if(node->left==NULL && node->right==NULL)
        sum = sum*10+node->val;
    return sum;
}

int sumNumbers(struct TreeNode* root) {
    return sumRecursively(root, 0);
}

int main() {
    
    return 0;
}
