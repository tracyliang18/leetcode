#Definition for a  binary tree node
# import heapq
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        visit_queue = []
        ready_queue = []
        res = []
        if root is None:
            return res
        ready_queue.append(root)
        while len(ready_queue) > 0:
            visit_queue = ready_queue
            ready_queue = []
            curlevel = []
            for n in visit_queue:
                curlevel.append(n.val)
                if n.left is not None:
                    ready_queue.append(n.left)
                if n.right is not None:
                    ready_queue.append(n.right)
            res.append(curlevel)
        res = res[::-1]
        return res


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n6 = TreeNode(6)
n7 = TreeNode(7)
n15 = TreeNode(15)

n1.left = n2
n1.right = n3
n3.left = n6
n3.right = n7
n7.right = n15

so = Solution()
print so.levelOrderBottom(n1)




