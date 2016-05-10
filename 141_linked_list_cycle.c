#include <assert.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

int hasCycle(struct ListNode *head) {
    if(head==NULL)
        return 0;

    struct ListNode *slow=head, *fast = head->next;

    while(fast!=NULL && fast->next!=NULL) {
        if(fast == slow)
            return 1;

        slow = slow->next;
        fast = fast->next->next;
    }

    return 0;
}

int main() {
    struct ListNode *head = (struct ListNode *)malloc(sizeof(struct ListNode *));
    head->val = 1;
    struct ListNode *node2 = (struct ListNode *)malloc(sizeof(struct ListNode *));
    node2->val = 2;
    struct ListNode *node3 = (struct ListNode *)malloc(sizeof(struct ListNode *));
    node3->val = 3;
    head->next = node2;
    node2->next = node3;
    node3->next = head;

    assert(hasCycle(head) == 1);

    node2->next = NULL;
    assert(hasCycle(head) == 0);

    return 0;
}
