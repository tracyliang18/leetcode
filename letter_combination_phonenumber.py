class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        letters = [" ","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        n = len(digits)
        cur_com = []
        Res = []


        def solve(r):
            if r == n:
                s = ''.join(cur_com)
                Res.append(s)
                return
            for l in letters[int(digits[r])]:
                cur_com.append(l)
                solve(r+1)
                cur_com.pop(-1)

        solve(0)
        return Res


so = Solution()
print so.letterCombinations("2")
