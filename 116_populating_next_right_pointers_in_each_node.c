#include <assert.h>
#include <stdlib.h>

struct TreeLinkNode {
    int val;
    struct TreeLinkNode *left, *right, *next;
};

void connect(struct TreeLinkNode *root) {
    if(root == NULL) return;

    struct TreeLinkNode* cur;
    while(root->left) {
        cur = root;
        while(cur) {
            cur->left->next = cur->right;
            if(cur->next)
                cur->right->next = cur->next->left;
            cur = cur->next;
        }
        root = root->left;
    }
}

int main() {
    struct TreeLinkNode* root = (struct TreeLinkNode *)malloc(sizeof(struct TreeLinkNode));
    root->val = 1;
    root->next = NULL;
    struct TreeLinkNode* node1_1 = (struct TreeLinkNode *)malloc(sizeof(struct TreeLinkNode));
    node1_1->val = 2;
    root->left = node1_1;
    struct TreeLinkNode* node1_2 = (struct TreeLinkNode *)malloc(sizeof(struct TreeLinkNode));
    node1_2->val = 3;
    node1_2->next = NULL;
    root->right = node1_2;
    struct TreeLinkNode* node2_1 = (struct TreeLinkNode *)malloc(sizeof(struct TreeLinkNode));
    node2_1->val = 4;
    node2_1->left = node2_1->right = NULL;
    struct TreeLinkNode* node2_2 = (struct TreeLinkNode *)malloc(sizeof(struct TreeLinkNode));
    node2_2->val = 5;
    node2_2->left = node2_2->right = NULL;
    struct TreeLinkNode* node2_3 = (struct TreeLinkNode *)malloc(sizeof(struct TreeLinkNode));
    node2_3->val = 6;
    node2_3->left = node2_3->right = NULL;
    struct TreeLinkNode* node2_4 = (struct TreeLinkNode *)malloc(sizeof(struct TreeLinkNode));
    node2_4->val = 7;
    node2_4->left = node2_4->right = node2_4->next = NULL;
    node1_1->left = node2_1;
    node1_1->right = node2_2;
    node1_2->left = node2_3;
    node1_2->right = node2_4;

    connect(root);
    assert(node1_1->next == node1_2);
    assert(node2_1->next == node2_2);
    assert(node2_2->next == node2_3);
    assert(node2_3->next == node2_4);
    assert(node2_4->next == NULL);

    return 0;
}
