class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        start = 0
        end = len(height) - 1
        ans = 0
        while start <= end - 2:
            if height[start] > height[start+1]:
                down = start + 1
                while down <= end  and height[down] < height[start]:
                    down += 1
                if down <= end - 1:
                    up = down
                    while up <= end - 1 and height[up + 1] >= height[up] and height[up] <= height[start]:
                        up += 1
                    if up <= end - 1:
                        if height[up] > height[start]:
                            min_height = height[start]
                        else:
                            min_height = height[up]
                    else:
                        min_height = height[up]
                    trap_start = start
                    while height[trap_start] > min_height:
                        trap_start += 1
                    total_water = min_height * (up - trap_start)
                    total_water -= sum(height[trap_start:up])
                    #print trap_start, down, up
                    #print min_height
                    #print total_water
                    ans += total_water
                    start = up
                else:
                    break
            else:
                start += 1

        return ans

sol = Solution()
print sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print sol.trap([5,4,1,2])
