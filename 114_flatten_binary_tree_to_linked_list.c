#include <assert.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

void flatten(struct TreeNode* root) {
    if(root==NULL || (root->left==NULL&&root->right==NULL))
        return;

}

int main() {

    return 0;
}
