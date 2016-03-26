class Node(object):
    def __init__(self):

        self.value = None

        self.left = None

        self.right = None

class Solution(object):

    def dfs(self,node,val):

        if node.left == None:

            self.ans.append(val)

        else:

            self.dfs(node.left,val * node.right.value)

            self.dfs(node.right,val * node.left.value)

    def build_tree(self,start, end):

        """

            return node

        """

        if start == end:

            node = Node()

            node.value = self.nums[start]

        else:

            mid = (end + start) / 2

            node = Node()

            node.left = self.build_tree(start,mid)

            node.right = self.build_tree(mid+1,end)

            node.value = node.left.value * node.right.value

        return node



    def productExceptSelf(self, nums):

        """

        :type nums: List[int]

        :rtype: List[int]

        """

        self.nums = nums

        tree = self.build_tree(0,len(nums)-1)

        self.ans = []

        self.dfs(tree,1)

        return self.ans


sol = Solution()
print sol.productExceptSelf([1,2,3,4])
