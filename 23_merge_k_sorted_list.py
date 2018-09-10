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
        head = ListNode(0)
        tail = head

        while True:
            min_value = float("inf")
            min_index = -1

            for i in range(len(lists)):
                list_node = lists[i]
                if list_node:
                    all_nodes_are_empty = False
                    if min_index == -1:
                        min_index = i
                        min_value = list_node.val
                    elif list_node.val < min_value:
                        min_value = list_node.val
                        min_index = i

            if min_index == -1:
                break

            tail.next = ListNode(min_value)
            tail = tail.next

            lists[min_index] = lists[min_index].next

        return head.next


list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

list3 = ListNode(2)
list3.next = ListNode(6)


merge_list = Solution().mergeKLists([list1, list2, list3])
node = merge_list
while node:
    print node.val
    node = node.next