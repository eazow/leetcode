#include <assert.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

int getListLength(struct ListNode *head) {
    int length = 0;
    struct ListNode *current = head;
    while(current) {
        current = current->next;
        length++;
    }
    return length;
}

struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    if(headA==NULL || headB==NULL)
        return NULL;

    int listALength = getListLength(headA);
    int listBLength = getListLength(headB);


    struct ListNode *pA=headA, *pB=headB;
    int i = 0;
    if(listALength >= listBLength)
        for(i = 0,pA = headA; i < listALength-listBLength; i++) 
            pA = pA->next;
    else
        for(i = 0,pB = headB; i < listBLength-listALength; i++)
            pB = pB->next;

    while(pA && pB) {
        if(pA == pB)
            return pA;
        pA = pA->next;
        pB = pB->next;
    }
    return NULL;
}

int main() {
    struct ListNode *headA = malloc(sizeof(struct ListNode));
    headA->val = 1;

    struct ListNode *headB = malloc(sizeof(struct ListNode));
    headB->val = 2;

    struct ListNode *node1 = malloc(sizeof(struct ListNode));
    node1->val = 3;

    struct ListNode *node2 = malloc(sizeof(struct ListNode));
    node2->val = 4;

    headA->next = node1;
    node1->next = node2;

    headB->next = node2;

    assert(getIntersectionNode(headA, headB) == node2);

    return 0;
}
