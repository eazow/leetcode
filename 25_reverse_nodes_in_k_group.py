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
        current = head
        while current:
            nodes.append(current)
            current = current.next

        if len(nodes) == 0:
            return None
        elif len(nodes) < k:
            return head

        reverse_nodes_head = ListNode(0)
        reverse_nodes_tail = reverse_nodes_head

        i = 1
        while i * k <= len(nodes):
            index = k * i - 1
            while index >= k * (i - 1):
                reverse_nodes_tail.next = nodes[index]
                reverse_nodes_tail = reverse_nodes_tail.next
                index -= 1
            i += 1

        if len(nodes) % k != 0:
            reverse_nodes_tail.next = nodes[k * (i - 1)]
        else:
            reverse_nodes_tail.next = None
        return reverse_nodes_head.next


assert Solution().reverseKGroup(None, 1) is None
assert Solution().reverseKGroup(ListNode(1), 2).val == 1

head_node = ListNode(1)
head_node.next = ListNode(2)
head_node.next.next = ListNode(3)
head_node.next.next.next = ListNode(4)
head_node.next.next.next.next = ListNode(5)

head_node = Solution().reverseKGroup(head_node, 2)

assert head_node.val == 2
assert head_node.next.val == 1
assert head_node.next.next.val == 4
assert head_node.next.next.next.val == 3
assert head_node.next.next.next.next.val == 5
