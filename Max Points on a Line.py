# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        # points = sorted(points, key=lambda p: (p.x, p.y))
        # for p in points:
        #     print p.x,p.y
        n=len(points)
        #print "len : ",n
        newpoints = []
        count = []
        i=0
        while i < n:
            j = i + 1
            c = 1
            while j < n and points[i].x == points[j].x and points[i].y == points[j].y:
                j += 1
                c += 1
            newpoints.append(points[i])
            count.append(c)
            i=j
        points = newpoints
        #print "new point"
        # for p in points:
        #     print p.x,p.y
        n = len(points)
        #print "new len",n
        if n == 1:
            return count[0]
        klist = []

        def calc_k(points):
            for a in xrange(n):
                for b in xrange(a+1,n):
                    xdiff = (points[a].x - points[b].x)
                    k = ((points[a].y - points[b].y)*1.0 / xdiff)  if xdiff != 0 else float('inf')
                    klist.append((k,a,b))

        calc_k(points)
        klist = sorted(klist)
        i=0
        curmax=0
        l = len(klist)
        while i < l:
            #print "i",i
            j=i+1
            indexset = set()
            indexset.add(klist[i][1])
            indexset.add(klist[i][2])
            while j < l and klist[j][0] == klist[i][0]:
                indexset.add(klist[j][1])
                indexset.add(klist[j][2])
                j += 1
            if j > i+1:
                union_set = UnionSet(indexset)
                for ind in xrange(i,j):
                    #get cur
                    union_set.union(klist[ind][1], klist[ind][2])
                setcount = {}
                for k in union_set.set:
                    setcount[k] = 0
                for k in union_set.set:
                    v=union_set.set[k]
                    setcount[v[0]] += count[k]
                cur=setcount[max(setcount, key=lambda k : setcount[k])]
            else:
                cur=count[klist[i][1]] + count[klist[i][2]]
            if cur>curmax:
                curmax = cur
            i = j

        return curmax


class UnionSet:
    def __init__(self,indexset):
        self.set = {}
        for i in indexset:
            self.set[i] = [i,0]

    def find(self,x):
        def find_x(x):
            if self.set[x][0] != x:
                self.set[x][0] = find_x(self.set[x][0])
            return self.set[x][0]
        return find_x(x)

    def union(self,x,y):
        xRoot = self.set[self.find(x)]
        yRoot = self.set[self.find(y)]

        if xRoot[0] == yRoot[0]:
            return
        if(xRoot[1] < yRoot[1]):
            xRoot[0] = yRoot[0]
        elif xRoot[1] > yRoot[1]:
            yRoot[0] = xRoot[0]
        else:
            yRoot[0] = xRoot[0]
            xRoot[1] += 1



def genPointList(array):
    pointsList=[]
    for i in array:
        p = Point(i[0],i[1])
        pointsList.append(p)
    return pointsList

# a=Point(1,1)
# a1 = Point(1,1)
# a2 = Point(1,1)
# b=Point(2,2)
# c=Point(3,3)
# pointSet = [a,b,c,a1,a2]
# su = Solution()
# print su.maxPoints(pointSet)
su = Solution()
array = [()]
pl = genPointList([(1,1),(1,1),(2,3)])
print su.maxPoints(pl)
# print 1 == None
# print -1 > None
# print 1 < None
# print float('inf')
# print 1 == float('inf')
# print 1000000000000000000000 < float('inf')
# print 1 > float('inf')





