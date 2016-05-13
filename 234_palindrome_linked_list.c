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
}

int main() {

    return 0;
}
