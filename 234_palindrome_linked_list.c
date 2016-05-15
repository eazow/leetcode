#include <assert.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

int isPalindrome(struct ListNode* head) {
    struct ListNode *slow=head, *fast=head;
    if(head==NULL || head->next==NULL)
        return 1;


    while(fast!=NULL&fast->next!=NULL;) {
        slow = slow->next;
        fast = fast->next->next;
    }

    struct ListNode *centerHead = NULL;
    if(fast == NULL)
        centerHead = reverseList(slow);
    else
        centerHead = reverseList(slow->next);
}

struct ListNode *reverseList(struct ListNode *head) {
    if(head == NULL || head->next ==NULL)
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
}

int main() {

    return 0;
}
