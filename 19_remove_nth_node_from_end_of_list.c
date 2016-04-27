#include <assert.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    struct ListNode* p1 = head;
    struct ListNode* newHead = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* p2 = newHead;
    p2->next = head;

    for(; p1 != NULL; p1=p1->next, n--) {
        if(n <= 0)
            p2 = p2->next;
    }
    struct ListNode* temp = p2->next;
    p2->next = p2->next->next;
    free(temp);

    return newHead->next;
}

int main() {
    struct ListNode* head = (struct ListNode *)malloc(sizeof(struct ListNode*));
    head->val = 1;
    struct ListNode* node = (struct ListNode *)malloc(sizeof(struct ListNode*));
    node->val = 2;
    head->next = node;
    node->next = NULL;

    assert(removeNthFromEnd(head, 2) == node);

    return 0;
}
