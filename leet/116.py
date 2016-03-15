# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        def pro(node):
            if node.left:
                if node.right:
                    node.left.next = node.right
                else:
                    node.left.next = None
                pro(node.left)

            if node.right:
                if node.next:
                    node.right.next = node.next.left
                else:
                    node.right.next = None
                pro(node.right)

        if root:
            root.next = None
            pro(root)
