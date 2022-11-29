from common.importing import import_class
from common.list import create_list


Solution = import_class("61_rotate_list", "Solution")


def test_rotate_empty_list():
    assert Solution().rotateRight(None, 100) is None


def test_rotate_list():
    head = create_list([0, 1, 2])
    head = Solution().rotateRight(head, 4)
    assert head.val == 2
    assert head.next.val == 0
    assert head.next.next.val == 1
