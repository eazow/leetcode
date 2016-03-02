#include <stdlib.h>
#include <assert.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

int isSameTree(struct TreeNode *p, struct TreeNode *q) {
    if(p==NULL && q==NULL) {
        return 1;
    }
    if(p!=NULL && q!=NULL && (p->val==q->val)) {
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
    return 0;
}

int main(int argc, char *argv[]) {
    struct TreeNode *root1 = malloc(sizeof(struct TreeNode));
    struct TreeNode *root2 = malloc(sizeof(struct TreeNode));
    root1->val = 1;
    root2->val = 1;

    assert(isSameTree(root1, root2));

    return 0;
}
