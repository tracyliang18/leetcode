# [::1] is a reverse trick
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        sreversed = []
        for w in s.split():
            sreversed.append(w)
        return ' '.join(sreversed[::-1])

su = Solution()
print su.reverseWords("this is a test")