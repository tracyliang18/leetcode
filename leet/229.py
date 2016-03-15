class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        ind = 0
        l = len(nums)
        ans = l + 1
        sum = 0
        prevend = -1
        while ind < l:
            if ind > 0:
                sum -= nums[ind - 1]
            end = prevend
            while end+1 < l and sum < s:
                end += 1
                sum += nums[end]
            if sum >= s:
                ans = min(ans, end - ind + 1)
                if ans == 1:
                    break
            else:
                break
            prevend = end
            ind += 1


        if ans == l + 1:
            ans = 0
        return ans



sol = Solution()
print sol.minSubArrayLen(7,[7,1,1,2,4,7])
print sol.minSubArrayLen(7,[1,1,1,1,1,1,1])
