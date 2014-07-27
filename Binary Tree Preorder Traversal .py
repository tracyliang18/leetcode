# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        if root is None:
            return []
        res = []
        NodeStack = []
        NodeStack.append(root)
        while len(NodeStack) > 0:
            Cur = NodeStack[-1]
            del NodeStack[-1]
            res.append(Cur.val)
            if Cur.right is not None:
                NodeStack.append(Cur.right)
            if Cur.left is not None:
                NodeStack.append(Cur.left)

        return res

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)

t1.left = t2
t1.right = t3
t3.left = t4

so = Solution()
print so.preorderTraversal(t1)
