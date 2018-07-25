class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        """
        result_list = current = ListNode(0)
        carry = 0
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            temp_sum = l1_val + l2_val + carry
            if temp_sum >= 10:
                carry = 1
            else:
                carry = 0
            current.next = ListNode(temp_sum % 10)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            current.next = ListNode(1)

        return result_list.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
result_list = Solution().addTwoNumbers(l1, l2)
assert result_list.val == 7
assert result_list.next.val == 0
assert result_list.next.next.val == 8

l1 = ListNode(1)
l2 = ListNode(9)
l2.next = ListNode(9)
result_list = Solution().addTwoNumbers(l1, l2)
assert result_list.val == 0
assert result_list.next.val == 0
assert result_list.next.next.val == 1