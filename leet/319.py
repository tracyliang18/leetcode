import math
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(n))

sol = Solution()
print sol.bulbSwitch(3)
print sol.bulbSwitch(6)
