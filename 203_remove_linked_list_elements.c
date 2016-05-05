#include <assert.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* removeElements(struct ListNode* head, int val) {
    struct ListNode *pHead = (struct ListNode *)malloc(sizeof(struct ListNode));
    pHead->next = head;
    struct ListNode *pre, *cur;
    for(pre=pHead,cur=head; cur!=NULL; cur=cur->next) {
        if(cur->val == val)
            pre->next = cur->next;
        else
            pre = cur;
    }
    return pHead->next;
}       

int main() {
    struct ListNode* node1 = (struct ListNode*)malloc(sizeof(struct ListNode*));
    node1->val = 1;
    struct ListNode* node2 = (struct ListNode*)malloc(sizeof(struct ListNode*));
    node2->val = 2;
    node1->next = node2;
    node2->next = NULL;

    assert(removeElements(node1, 1) == node2);
    
    return 0;
}
