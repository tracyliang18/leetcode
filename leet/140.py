class Node(object):
    def __init__(self):
        self.next = {}
        self.key = None
        self.isend = False

    def _print(self):
        print self.key,self.isend

class Trie(object):
    def __init__(self, word_list):
        self.root = Node()
        self.root.key = ""
        self.root.isend = False

        for word in word_list:
            cur = self.root
            if len(word) > 0:
                for c in word:
                    if c in cur.next:
                        cur = cur.next[c]
                    else:
                        cur.next[c] = Node()
                        cur.next[c].key = cur.key + c
                        cur = cur.next[c]
                cur.isend = True

import copy
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        # #self.trie = Trie(list(wordDict))
        # self.ans = []
        # self.memo = {len(s):""}
        # def sentence(i):
        #     if i in memo:
        #         return memo[i]
        #     for j in range(i+1,len(s)+1):
        #         if s[i:j] in wordDict:
        #             memo[i] = []
        #             for tail in sentence(j):
        #                 if tail == "":
        #                     res = s[i:j]
        #                 else:
        #                     res = s[i:j] + " " + res
        memo = {len(s): ['']}
        def sentences(i):
            if i not in memo:
                memo[i] = [s[i:j] + (tail and ' ' + tail)
                           for j in range(i+1, len(s)+1)
                           if s[i:j] in wordDict
                           for tail in sentences(j)]
            print i,memo[i]
            return memo[i]
        return sentences(0)

sol = Solution()
wordset = set(["cat", "cats", "and", "sand", "dog"])
s = "catsandsssdog"

print sol.wordBreak(s,wordset)
