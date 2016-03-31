class Solution(object):

    def maxSlidingWindow(self, nums, k):

        """

        :type nums: List[int]

        :type k: int

        :rtype: List[int]

        """

        if len(nums) == 0:

            return []

        cur = []

        for ind,num enumerate(nums[0:k - 1]):

            while len(cur) > 0 and cur[-1][1] < num:

                del cur[-1]

            cur.append((ind,num))

        ret = []

        for i in range(len(nums) - k + 1):

            while len(cur) > 0 and cur[-1][1] < nums[i+k-1]:

                del cur[-1]

            cur.append((i+k-1,nums[i+k-1]))

            ret.append(cur[0][1])

            if cur[0][0] == i:

                del cur[0]



        return ret
