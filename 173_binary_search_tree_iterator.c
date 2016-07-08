#include <assert.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct BSTIterator {
    struct TreeNode** stack;
    int top;
    int size;
};

#define SIZE 1000

struct BSTIterator *bstIteratorCreate(struct TreeNode *root) {
    struct BSTIterator* iter = (struct BSTIterator *)malloc(sizeof(struct BSTIterator));
    iter->stack = (struct TreeNode **)malloc(sizeof(struct TreeNode *) * SIZE);
    iter->top = 0;
    iter->size = SIZE;

    while(root) {
        iter->stack[iter->top++] = root;
        root = root->left;
    }
    return iter;
}

int bstIteratorHasNext(struct BSTIterator *iter) {
    return iter->top > 0;
}

int bstIteratorNext(struct BSTIterator *iter) {
    struct TreeNode* node = iter->stack[--iter->top];
    int val = node->val;
    node = node->right;
    while(node) {
        iter->stack[iter->top++] = node;
        node = node->left;
    }
    return val;
}

void bstIteratorFree(struct BSTIterator *iter) {
    free(iter->stack);
    free(iter);
}

int main() {
    struct TreeNode* root = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    root->val = 2;
    struct TreeNode* node1_1 = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    node1_1->val = 1;
    node1_1->left = NULL;
    node1_1->right = NULL;
    root->left = node1_1;
    struct TreeNode* node1_2 = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    node1_2->val = 3;
    node1_2->left = NULL;
    node1_2->right = NULL;
    root->right = node1_2;

    struct BSTIterator *iter = bstIteratorCreate(root);
//  while(bstIteratorHasNext(iter))
//      bstIteratorNext(iter)
    assert(bstIteratorHasNext(iter) == 1);
    assert(bstIteratorNext(iter) == 1);
    assert(bstIteratorNext(iter) == 2);
    assert(bstIteratorNext(iter) == 3);
    assert(bstIteratorHasNext(iter) == 0);
    bstIteratorFree(iter);

    return 0;
}
