import random

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        self.values = values

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        rand_int = random.randint(0, len(self.values) - 1)
        return self.values[rand_int]

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

print Solution(head).getRandom()