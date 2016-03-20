#include <assert.h>
#include <stdlib.h>
#include <stdio.h>

struct ListNode {
	int val;
	struct ListNode *next;
};

struct ListNode *deleteDuplicates(struct ListNode *head) {
	if(head==NULL || head->next==NULL)
		return head;

	int pre_val = head->val;
	int val = head->next->val;
	struct ListNode *pre = head;
	struct ListNode *cur = head->next;

	while(cur) {
		pre_val = pre->val;
		val = cur->val;
		if(val == pre_val) 
			pre->next = cur->next;
		else 
			pre = pre->next;
		cur = cur->next;
	}
	return head;
}

int main(int argc, char **argv) {
	struct ListNode *node1 = malloc(sizeof(struct ListNode));
	node1->val = 1;
	struct ListNode *node2 = malloc(sizeof(struct ListNode));
	node2->val = 2;
	struct ListNode *node3 = malloc(sizeof(struct ListNode));
	node3->val = 2;
	node1->next = node2;
	node2->next = node3;
	node3->next = NULL;
	deleteDuplicates(node1);
	assert(node1->next == node2);
	assert(node2->next == NULL);
}
