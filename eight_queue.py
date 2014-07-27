class Solution:
    # @return a list of lists of string
    def __init__(self):
        self.resCnt = 0
    def solveNQueens(self, n):
        #print space

        Res = []
        isColFill = [0 for x in xrange(n)]
        space = [[0 for x in xrange(n)] for x in xrange(n)]
        def validateIntersect(x,y):
            X,Y = x,y
            #check I direction, ordered by Quadrant
            while X >= 0  and Y < n:
                if space[X][Y] == 1:
                    return False
                X -= 1
                Y += 1
            #check II direction, ordered by Quadrant
            X,Y = x,y
            while X >=0 and Y >= 0:
                if space[X][Y] == 1:
                    return False
                X -= 1
                Y -= 1
            #check III direction, ordered by Quadrant
            X,Y = x,y
            while X < n and Y >= 0:
                if space[X][Y] == 1:
                    return False
                X += 1
                Y -= 1
            #check IV direction, ordered by Quadrant
            X,Y = x,y
            while X < n and Y < n:
                if space[X][Y] == 1:
                    return False
                X += 1
                Y += 1
            return True

        def validatePos(x,y):
            #print "pos",x,y
            #check row and intersect
            if not any(space[x]) and validateIntersect(x,y):
                return True
            return False

        def fillCol(r):
            #print "col",r
            if r == n:
                self.resCnt += 1
                thisRes = []
                for x in xrange(n):
                    row=""
                    for y in xrange(n):
                        row = row + ("Q" if space[x][y] == 1 else ".")
                        #print row
                    thisRes.append(row)
                Res.append(thisRes)
                return


            for x in xrange(n):
                if validatePos(x, r):
                    isColFill[r] = 1
                    space[x][r] = 1
                    fillCol(r+1)
                    isColFill[r] = 0
                    space[x][r] = 0


        fillCol(0)
        #print self.resCnt
        return Res



so = Solution()
print so.solveNQueens(4)
