class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        self.nodes = {}

        def traverse(node, row, column):
            if row not in self.nodes:
                self.nodes[row] = []


            if node:
                self.nodes[row].append(node.val)
                traverse(node.left, row + 1, column)
                traverse(node.right, row + 1, column + 1)
            else:
                self.nodes[row].append("")

        traverse(root, 0, 0)

        print self.nodes


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
Solution().printTree(root)
