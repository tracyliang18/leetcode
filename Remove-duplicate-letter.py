from collections import defaultdict
class Solution(object):
    def removeDuplicateLetters(self, s):
        counter = defaultdict(lambda : 0)
        for c in s:
            counter[c] += 1
        stack = []
        used = set()
        for c in s:
            counter[c] -= 1
            if c in used:
                continue
            used.add(c)
            ind = len(stack) - 1
            while ind >= 0 and stack[ind] > c and counter[stack[ind]] > 0:
                used.remove(stack[ind])
                del stack[ind]
                ind -= 1
            stack.append(c)
        return "".join(stack)
    # def removeDuplicateLetters(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """
    #     def get_leftmost_pos(start, end, c):
    #         pos = char_pos[c]
    #         if pos[-1] < start:
    #             return -1
    #         if pos[0] > end:
    #             return -1
    #         l = len(pos)
    #         b = 0
    #         e = l - 1
    #
    #         while b < e:
    #             mid = (b + e) / 2
    #             if pos[mid] < start:
    #                 b = mid + 1
    #             else:
    #                 e = mid
    #         return pos[e]
    #
    #     def dfs(level,segments):
    #         print level,segments
    #         if level == len(chars):
    #             cur = "".join(map(lambda ind: s[ind],segments[1:-1]))
    #             if cur < self.ans:
    #                 self.ans = cur
    #             return
    #         c = chars[level]
    #         ind = 0
    #         l = len(segments)
    #         while ind < l - 1:
    #             p = get_leftmost_pos(segments[ind]+1, segments[ind+1]-1, c)
    #             if p != -1:
    #                 new_segments = segments[0:ind+1] + [p] + segments[ind+1:]
    #                 dfs(level+1, new_segments)
    #             ind += 1
    #
    #
    #     char_pos = defaultdict(lambda : [])
    #     for ind,c in enumerate(s):
    #         char_pos[c].append(ind)
    #     chars = char_pos.keys()
    #     chars.sort()
    #     self.ans = "".join(reversed(chars))
    #
    #     dfs(0, [-1,len(s)])
    #     print self.ans
    #     return self.ans

o = Solution()
print o.removeDuplicateLetters("abcd")
print o.removeDuplicateLetters("abcdefghijklmnopqrstuvwxyz")
