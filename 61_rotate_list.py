from common.list import ListNode, get_length_and_tail


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        length, tail = get_length_and_tail(head)
        k = k % length
        steps = length - k - 1
        cur = head
        while steps > 0:
            cur = cur.next
            steps -= 1

        tail.next, head, cur.next = head, cur.next, None

        return head
