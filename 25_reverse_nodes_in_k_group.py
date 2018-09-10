class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :param head: ListNode
        :param k: int
        :return: ListNode
        """
        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        reverse_nodes_head = nodes[k - 1]
        reverse_nodes_tail = reverse_nodes_head

        while k >= 2:
            reverse_nodes_tail.next = nodes[k - 2]
            reverse_nodes_tail = reverse_nodes_tail.next
            k -= 1
        reverse_nodes_tail.next = nodes[k]

        return reverse_nodes_head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

head = Solution().reverseKGroup(head, 3)
assert head.val == 3
assert head.next.val == 2
assert head.next.next.val == 1
assert head.next.next.next.val == 4
assert head.next.next.next.next.val == 5
