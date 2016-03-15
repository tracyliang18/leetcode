# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.total_level = -1
        def dfs_right_first(level,root):
            if root:
                if level > self.total_level:
                    self.total_level = level
                    ans.append(root.val)
                if root.right:
                    dfs_right_first(level + 1, root.right)
                if root.left:
                    dfs_right_first(level + 1, root.left)
        #total_level = -1
        ans = []
        dfs_right_first(0, root)
        return ans

def make_node(ind, array): # leftchild 2*x, right 2*x+1
    if len(array) < ind + 1:
        return None
    node = TreeNode(array[ind])
    if 2*ind < len(array) and array[2*ind]:
        node.left = make_node(2*ind, array)
    if 2*ind+1 < len(array) and array[2*ind+1]:
        node.right = make_node(2*ind+1, array)
    return node

tree = make_node(1, [0, 1,2,3,None,5,None,4])
sol = Solution()
print sol.rightSideView(tree)
