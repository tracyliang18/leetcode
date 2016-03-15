import copy
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        def make_node(pre_start, pre_end, in_start, in_end):
            #print pre_start, pre_end, in_start, in_end
            preorder_len = pre_end - pre_start + 1
            if preorder_len > 0:
                node = TreeNode(self.preorder[pre_start])
                #find curnode in inorder
                ind = in_start
                while ind <= in_end:
                    if self.inorder[ind] == self.preorder[pre_start]:
                        break
                    ind += 1
                new_left_len = ind - in_start
                new_right_len = in_end - ind
                #print new_left_len,new_right_len
                node.left = make_node(pre_start + 1, pre_start + new_left_len, in_start, in_start + new_left_len - 1)
                node.right = make_node(pre_end - new_right_len + 1, pre_end, in_end - new_right_len + 1, in_end)
                return node
            else:
                return None

        self.preorder = preorder
        self.inorder = inorder
        tree = make_node(0, len(self.preorder) - 1, 0, len(self.inorder) - 1)
        return tree

def dfs_print(tree):
    if tree:
        print tree.val
        dfs_print(tree.left)
        dfs_print(tree.right)

sol = Solution()
res = sol.buildTree([9],[9])
dfs_print(res)
