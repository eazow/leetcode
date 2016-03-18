#include <stdlib.h>
#include <assert.h>
#include <stdio.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode *oddEvenList(struct ListNode *head) {
    struct ListNode *current, *even, *even_head;

    if(head==NULL || head->next==NULL || head->next->next==NULL)
        return head;

    for(current = head, even=head->next, even_head=head->next; current&&current->next; current=current->next) {
        if(current!=head) {
            even->next = current->next;
            even = even->next;
        }
        if(current->next->next) 
            current->next = current->next->next;
        else
            break;
    }
    even->next = NULL;
    current->next = even_head;
    return head;
}

int main(int argc, char *argv[]) {
    struct ListNode *node;
    struct ListNode *node1 = malloc(sizeof(struct ListNode));
    node1->val = 1;
    struct ListNode *node2 = malloc(sizeof(struct ListNode));
    node2->val = 2;
    struct ListNode *node3 = malloc(sizeof(struct ListNode));
    node3->val = 3;
    struct ListNode *node4 = malloc(sizeof(struct ListNode));
    node4->val = 4;
    struct ListNode *node5 = malloc(sizeof(struct ListNode));
    node5->val = 5;
    struct ListNode *node6 = malloc(sizeof(struct ListNode));
    node6->val = 6;
    node1->next = node2;
    node2->next = node3;
    node3->next = node4;
    node4->next = node5;
    node5->next = node6;

    node1 = oddEvenList(node1);
    assert(node1->next == node3);
    assert(node3->next == node5);
    assert(node5->next == node2);
    assert(node2->next == node4);
    assert(node4->next == node6);

    return 0;
}
