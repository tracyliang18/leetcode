class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        high_low = dict()
        end = len(prices)
        if end <= 1:
            return 0
        i=1
        while i < end and prices[0] == prices[i]:
            i += 1
        if i == end:
            return 0
        high_low[0] = "high" if prices[0] > prices[i] else "low"
        cur = 0
        while i < end:
            if high_low[cur] == "high":
                while i < end and prices[i] <= prices[i - 1]:
                    i += 1
                high_low[i-1] = "low"
            else:
                while i < end and prices[i] >= prices[i - 1]:
                    i += 1
                high_low[i-1] = "high"
            cur = i - 1
        key = sorted(high_low.iteritems())
        #print key
        res=0
        for x in xrange(len(key) - 1):
            if key[x][1] == 'low':
                res +=prices[key[x+1][0]] -  prices[key[x][0]]
        return res
so = Solution()
print so.maxProfit([1,1,2,3,4,3,2,5,6,7,8,4,3,2,1])




