from collections import defaultdict
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        word_set = defaultdict(int)
        for w in words:
            word_set[w] += 1
        word_cnt = len(words)
        ans = []
        if len(words) > 0:
            wordlen = len(words[0])

        for j in range(wordlen):
            ind = j
            prev_break = True
            while ind + word_cnt * wordlen <= len(s):
                #print ind
                if prev_break:
                    mark = defaultdict(int)
                    prev_break = False
                    #print ind
                    i = 0
                    while i < word_cnt:
                        cur = s[ind + wordlen * i:ind + wordlen * (i+1)]
                        if cur in word_set:
                            mark[cur] += 1
                        else:
                            ind = ind + wordlen * (i+1)
                            prev_break = True
                            break
                        i += 1
                    if not prev_break:
                        ok = True
                        for w in word_set:
                            if word_set[w] != mark[w]:
                                ok = False
                                break
                        if ok:
                            ans.append(ind)
                        ind += wordlen
                else:
                    cur = s[ind + (word_cnt - 1) * wordlen:ind + word_cnt * wordlen]
                    mark[s[ind - wordlen:ind]] -= 1
                    if cur in word_set:
                        mark[cur] += 1
                        ok = True
                        for w in word_set:
                            if word_set[w] != mark[w]:
                                ok = False
                                break
                        if ok:
                            ans.append(ind)
                        ind += wordlen
                    else:
                        ind = ind + word_cnt * wordlen
                        prev_break = True


        return ans

sol = Solution()
print sol.findSubstring("barfoothefoobarman",["foo", "bar","the"])
print sol.findSubstring("barfoothefoobarman",["foo", "bar"])
print sol.findSubstring("wordgoodgoodgoodbestword",
["word","good","best","good"])
