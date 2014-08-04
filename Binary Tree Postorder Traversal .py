# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        p = root
        res = []
        nodestack = []
        while True:
            while(p):
                nodestack.append(p)
                p = p.left
            while len(nodestack) > 0 and nodestack[-1].right == p:
                p = nodestack.pop()
                res.append(p.val)
            if len(nodestack) <= 0:
                break
            p = nodestack[-1].right
        return res