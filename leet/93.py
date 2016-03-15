import copy

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.ans = []
        total = len(s)
        def dfs(level, start, curres):
            if level == 4:
                if start == total:
                    self.ans.append(".".join(curres))
                else:
                    return

            if total - start > (4 - level) * 3:
                return
            if total - start < (4 - level):
                return
            offset = 1
            while offset <= 3:
                if start + offset <= total:
                    cur = s[start:start+offset]
                    cur_i = int(cur)
                    if (cur_i > 0 and cur_i <= 255 and cur[0] != '0') or (cur_i == 0 and offset == 1):
                        newres = copy.copy(curres)
                        newres.append(cur)
                        dfs(level+1, start + offset, newres)
                else:
                    break
                offset += 1

        dfs(0,0,[])
        return self.ans

sol = Solution()
print sol.restoreIpAddresses("25525511135")
print sol.restoreIpAddresses("00525511135")
print sol.restoreIpAddresses("00525511131231235")
print sol.restoreIpAddresses("000")
print sol.restoreIpAddresses("00001")
