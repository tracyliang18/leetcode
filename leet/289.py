class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        modified_set = set()
        Y = len(board)
        if Y:
            X = len(board[0])
        def fill_xy(x,y):
            cnt = 0
            for ox in (-1,0,1):
                for oy in (-1,0,1):
                    curx = x + ox
                    cury = y + oy
                    if curx >= 0 and curx < X and \
                        cury >= 0 and cury < Y and \
                         (curx != x or cury != y):

                        if cury*X + curx not in modified_set:
                            cnt += board[cury][curx]
                        else:
                            cnt += 1 - board[cury][curx]

            #print y,x,cnt
            if board[y][x]:
                if cnt < 2 or cnt > 3:
                    board[y][x] = 0
                    modified_set.add(y*X+x)

            else:
                if cnt == 3:
                    board[y][x] = 1
                    modified_set.add(y*X+x)

        if X and Y:
            for x in xrange(X):
                for y in xrange(Y):
                    fill_xy(x,y)

board = [[1,1,1],
         [1,1,1],
         [1,1,1]]

sol = Solution()
print board
sol.gameOfLife(board)
print board
