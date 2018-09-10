class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :param lists: List[ListNode]
        :return: ListNode
        """
        nums = []
        for list_node in lists:
            current = list_node
            while current:
                nums.append(current.val)
                current = current.next

        nums.sort()

        head = ListNode(0)
        tail = head
        for num in nums:
            tail.next = ListNode(num)
            tail = tail.next

        return head.next


list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

list3 = ListNode(2)
list3.next = ListNode(6)

head_node = Solution().mergeKLists([list1, list2, list3])
assert head_node.val == 1
assert head_node.next.val == 1
assert head_node.next.next.val == 2
assert head_node.next.next.next.val == 3
assert head_node.next.next.next.next.val == 4
assert head_node.next.next.next.next.next.val == 4
assert head_node.next.next.next.next.next.next.val == 5
assert head_node.next.next.next.next.next.next.next.val == 6
