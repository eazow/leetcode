#include <assert.h>
#include <stdlib.h>

/**
 * Definition for singly-linked lsit.
 */
struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode *swapPairs(struct ListNode *head) {    
    if(head==NULL || head->next==NULL)
        return head;

    struct ListNode *node1 = head;
    struct ListNode *node2 = head->next;
    struct ListNode *node3 = NULL;

    node3 = node2->next;
    node2->next = node1;
    node1->next = node3;
    head = node2;
    node1->next = swapPairs(node1->next);

    return head;
}

int main() {
    struct ListNode *node1 = malloc(sizeof(struct ListNode));
    struct ListNode *node2 = malloc(sizeof(struct ListNode));
    struct ListNode *node3 = malloc(sizeof(struct ListNode));
    struct ListNode *node4 = malloc(sizeof(struct ListNode));
    node1->val = 1;
    node2->val = 2;
    node3->val = 3;
    node4->val = 4;
    node1->next = node2;
    node2->next = node3;
    node3->next = node4;
    node4->next = NULL;

    node1 = swapPairs(node1);
    assert(node1->val == 2);
    assert(node1->next->val == 1);
    assert(node1->next->next->val == 4);
    assert(node1->next->next->next->val == 3);

    return 0;
}
