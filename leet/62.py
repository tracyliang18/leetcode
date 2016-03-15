class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1:
            return 1
        r = [i+1 for i in range(n)]
        for t in range(m-2):
            for j in range(n-1):
                r[j+1] = r[j] + r[j+1]
        return r[n-1]

o = Solution()
print o.uniquePaths(2 ,3)
