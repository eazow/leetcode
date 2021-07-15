from common.list import create_list


import importlib
rotate_list = importlib.import_module("61_rotate_list")


def test_rotate_empty_list():
    assert rotate_list.Solution().rotateRight(None, 100) is None


def test_rotate_list():
    head = create_list([0, 1, 2])
    head = rotate_list.Solution().rotateRight(head, 4)
    assert head.val == 2
    assert head.next.val == 0
    assert head.next.next.val == 1
