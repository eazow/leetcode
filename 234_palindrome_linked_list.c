#include <assert.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode *reverseList(struct ListNode *head) {
    if(head == NULL || head->next == NULL)
        return head;

    struct ListNode *pre = head;
    struct ListNode *cur = head->next;
    struct ListNode *next = cur->next;
    while(next != NULL) {
        cur->next = pre;
        pre = cur;
        cur = next;
        next = next->next;
    }
    head->next = NULL;

    return cur;
}

int isPalindrome(struct ListNode* head) {
    struct ListNode *slow=head, *fast=head;
    if(head==NULL || head->next==NULL)
        return 1;

    int i = 0;
    while(fast!=NULL & fast->next!=NULL) {
        slow = slow->next;
        fast = fast->next->next;
        i++;
    }

    struct ListNode *tail = NULL;
    if(fast == NULL)
        tail = reverseList(slow);
    else
        tail = reverseList(slow->next);

    int j = 0;
    struct ListNode *node1 = head;
    struct ListNode *node2 = tail;
    while(j < i) {
        if(node1->val != node2->val)
            return 0;
        node1 = node1->next;
        node2 = node2->next;
    }
    return 1;
}

int main() {
    struct ListNode *head = (struct ListNode *)malloc(sizeof(struct ListNode *));
    head->val = 1;

    struct ListNode *node2 = (struct ListNode *)malloc(sizeof(struct ListNode *));
    node2->val = 2;
    head->next = node2;

    struct ListNode *node3 = (struct ListNode *)malloc(sizeof(struct ListNode *));
    node3->val = 1;
    node2->next = node3;
    node3->next = NULL;

    assert(isPalindrome(head) == 1);

    return 0;
}
