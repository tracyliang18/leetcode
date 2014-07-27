#from collections import Counter
#from collections import defaultdict
class Solution:
    # @return a string
    def minWindow(self, S, T):
        targetCounter = dict()
        for c in T:
            if c not in targetCounter:
                targetCounter[c] = 1
            else:
                targetCounter[c] += 1
        #print targetCounter
        # tCharSet = set()
        # for c in T:
        #     tCharSet.add(c)
        #print tCharSet
        finishCnt = 0
        tCharCnt = len(targetCounter)
        getTCharPos = {}
        for c in T:
            getTCharPos[c] = []

        cpos=0
        cend = len(S)
        resmin = 1000000
        resstart = -1
        resend = -1
        while cpos < cend:
            #print "curpos",cpos
            if S[cpos] in T:
                getTCharPos[S[cpos]].append(cpos)
                if len(getTCharPos[S[cpos]]) == targetCounter[S[cpos]]:
                    finishCnt += 1
                if (len(getTCharPos[S[cpos]])) > targetCounter[S[cpos]]:
                    del getTCharPos[S[cpos]][0]
                if(finishCnt == tCharCnt):
                    #print "finish",getTCharPos
                    minItemKey = min(getTCharPos, key=lambda k : getTCharPos[k][0])
                    #print "minItemKey",minItemKey
                    start = getTCharPos[minItemKey][0]
                    #print "start",start
                    del getTCharPos[minItemKey][0]
                    end = cpos
                    #print "end",end
                    curmin = end - start + 1
                    if(curmin < resmin):
                        resmin = curmin
                        resstart = start
                        resend = end
                    finishCnt -= 1
            cpos += 1
        #print "resstart",resstart,resend
        if resstart != -1:
            return S[resstart:resend+1]
        else:
            return ""




so = Solution()
print so.minWindow("ADOBECODEBANC","ABC")
