from Queue import Queue

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right =None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype int
        """
        queue = Queue()
        queue.put(root)
        node = None
        while not queue.empty():
            node = queue.get()
            if node.right:
                queue.put(node.right)
            if node.left:
                queue.put(node.left)

        return node.val


root = TreeNode(2)
left = TreeNode(1)
right = TreeNode(3)
root.left = left
root.right = right
Solution().findBottomLeftValue(root) == 1

root = TreeNode(1)
node1_1 = TreeNode(2)
node1_2 = TreeNode(3)
node2_1 = TreeNode(4)
node2_2 = TreeNode(5)
node2_3 = TreeNode(6)
node3_1 = TreeNode(7)
root.left = node1_1
root.right = node1_2
node1_1.left = node2_1
node1_2.left = node2_2
node1_2.right = node2_3
node2_2.left = node3_1
Solution().findBottomLeftValue(root) == 7