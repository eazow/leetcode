#include <stdlib.h>
#include <assert.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

void deleteNode(struct ListNode *node) {
    node->val = node->next->val;
    struct ListNode *next = node->next;
    node->next = node->next->next;
    free(next);
}

int main(int c, char *argv[]) {
    struct ListNode *node1 = malloc(sizeof(struct ListNode));
    node1->val = 1;
    struct ListNode *node2 = malloc(sizeof(struct ListNode));
    node2->val = 2;
    node1->next = node2;
    struct ListNode *node3 = malloc(sizeof(struct ListNode));
    node3->val = 3;
    node2->next = node3;

    deleteNode(node2);
    assert(node1->next->val==3);
}
