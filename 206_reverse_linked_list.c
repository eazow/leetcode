#include <assert.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode *reverseList(struct ListNode *head) {
    int i = 0;
    struct ListNode *current, *previous, *next;
    if(head==NULL)
        return head;
    for(previous = head,current=head->next; current != NULL; previous=current,current=next) {
        next = current->next?current->next:NULL;
        current->next = previous;
    }
    head->next = NULL;
    return previous;
}

int main(int argc, char *argv[]) {
    struct ListNode *node1 = malloc(sizeof(struct ListNode));
    node1->val = 1;
    struct ListNode *node2 = malloc(sizeof(struct ListNode));
    node2->val = 2;
    struct ListNode *node3 = malloc(sizeof(struct ListNode));
    node3->val = 3;
    node1->next = node2;
    node2->next = node3;

    struct ListNode *head = reverseList(node1);
    assert(head->val == 3);
    assert(head->next->val == 2);
    assert(head->next->next->val == 1);
}
