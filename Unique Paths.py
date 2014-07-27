class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        mat = [[1 for x in xrange(n)] for x in xrange(m)]
        for col in xrange(n-2, -1, -1):
            for row in xrange(m-2,-1,-1):
                #print row,col
                mat[row][col] = mat[row+1][col] + mat[row][col+1]
        return mat[0][0]


so = Solution()
print so.uniquePaths(3,4)