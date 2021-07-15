class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_list(values):
    head = None
    for v in values[::-1]:
        node = ListNode(v)
        node.next, head = head, node

    return head


def get_length_and_tail(head: ListNode) -> int:
    tail = head
    length = 1
    while tail.next:
        tail = tail.next
        length += 1
    return length, tail

