class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        def GenLine(cur):
            assert(len(cur) > 0)
            charCnt = sum(len(w) for w in cur)
            spaceCnt = L - charCnt
            if len(cur) == 1:
                Res.append(cur[0]+' '*spaceCnt)
                return
            else:
                spaceUnit = spaceCnt / (len(cur) - 1)
                remainder = spaceCnt % (len(cur) - 1)
            if remainder != 0:
                i = 0
                while remainder > 0:
                    remainder -= 1
                    cur[i] += ' '
                    i += 1
            curs = (spaceUnit*' ').join(cur)
            Res.append(curs)

        Res = []
        cur = []
        left = L
        for w in words:
            #print left
            if len(w) <= left:
                cur.append(w)
                left = left - len(w) - 1
            else:
                GenLine(cur)
                cur=[]
                left=L
                cur.append(w)
                left = left - len(w) - 1
        if len(cur) > 0:
            GenLine(cur)
        lastline = Res[-1].split()
        laststr = ' '.join(lastline)
        Res[-1] = laststr + ' '*(L - len(laststr))
        return Res

so = Solution()
words = ["Don't","go","around","saying","the","world","owes","you","a","living;","the","world","owes","you","nothing;","it","was","here","first."]
print so.fullJustify(words, 30)






