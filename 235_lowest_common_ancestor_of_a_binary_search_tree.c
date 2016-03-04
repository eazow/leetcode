#include <assert.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct TreeNode *lowestCommonAncestor(struct TreeNode *root, struct TreeNode *p, struct TreeNode *q) {
    while((p->val-root->val)*(q->val-root->val)>0) {
        root = p->val<root->val?root->left:root->right;
    }
    return root;
}

int main(int argc, char *argv[]) {
    struct TreeNode *root = malloc(sizeof(struct TreeNode));
    root->val = 6;
    struct TreeNode *left1_1 = malloc(sizeof(struct TreeNode));
    left1_1->val = 2;
    root->left = left1_1;
    struct TreeNode *left2_1 = malloc(sizeof(struct TreeNode));
    left2_1->val = 0;
    left1_1->left = left2_1;
    struct TreeNode *left2_2 = malloc(sizeof(struct TreeNode));
    left2_2->val = 4;
    left2_1->right = left2_2;

    struct TreeNode *right1_1 = malloc(sizeof(struct TreeNode));
    right1_1->val = 8;
    root->right = right1_1;

    assert(lowestCommonAncestor(root, left2_1, right1_1) == root);

}
