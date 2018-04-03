class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        while l1:
            num1 += l1.val
            l1 = l1.next
            num1 *= 10
        num1 = num1 / 10
        num2 = 0
        while l2:
            num2 += l2.val
            l2 = l2.next
            num2 *= 10
        num2 = num2 / 10
        the_sum = num1 + num2
        if the_sum == 0:
            return ListNode(0)

        nums = []
        while the_sum > 0:
            nums.append(the_sum % 10)
            the_sum = the_sum / 10

        next_node = None
        head_node = None
        for num in nums:
            head_node = ListNode(num)
            head_node.next = next_node
            next_node = head_node
        return head_node


l1 = ListNode(7)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

head_node = Solution().addTwoNumbers(l1, l2)
assert head_node.val == 7
assert head_node.next.val == 8
assert head_node.next.next.val == 0
assert head_node.next.next.next.val == 7