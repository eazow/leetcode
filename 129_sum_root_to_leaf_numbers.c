#include <assert.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

int sumRecursively(struct TreeNode* node, int sum) {
    if(node == NULL)
        return sum;
    else
        sum = sum*10+node->val;
    sum = sumRecursively(node->left, sum);
    sum = sumRecursively(node->right, sum);
    return sum;
}

int sumNumbers(struct TreeNode* root) {
    return sumRecursively(root, 0);
}

int main() {
    
    return 0;
}
