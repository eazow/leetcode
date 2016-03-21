#include <assert.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode *mergeTwoLists(struct ListNode *l1, struct ListNode *l2) {
    struct ListNode *head = malloc(sizeof(struct ListNode));
    struct ListNode *cur = head;
    struct ListNode *cur1 = l1; 
    struct ListNode *cur2 = l2;
    while(cur1 && cur2) {
        if(cur1->val < cur2->val) {
            cur->next = cur1;
            cur1 = cur1->next;
        }
        else {
            cur->next = cur2;
            cur2 = cur2->next;
        }
        cur = cur->next;
    }
    if(cur1) 
        cur->next = cur1;
    else if(cur2)
        cur->next = cur2;
    return head->next;
}

int main() {
    struct ListNode *node1 = malloc(sizeof(struct ListNode));
    node1->val = 1;
    struct ListNode *node10 = malloc(sizeof(struct ListNode));
    node10->val = 10;
    node1->next = node10;
    node10->next = NULL;

    struct ListNode *node2 = malloc(sizeof(struct ListNode));
    node2->val = 2;
    struct ListNode *node3 = malloc(sizeof(struct ListNode));
    node3->val = 3;
    node2->next = node3;
    node3->next = NULL;

    node1 = mergeTwoLists(node1, node2);

    assert(node1->next == node2);
    assert(node1->next->next == node3);
    assert(node1->next->next->next == node10);

    return 0;
}
