# class Solution:
#     # @param board, a 9x9 2D array
#     # @return a boolean
#     def isValidSudoku(self, board):
#         row0=slice(0,3)
#         row1=slice(3,6)
#         row2=slice(6,9)
#         col0=slice(0,9,3)
#         col1=slice(1,9,3)
#         col2=slice(2,9,3)
#
#         Rows=[]
#         Rows.append(board[0][row0]+board[1][row0]+board[2][row0])
#         Rows.append(board[0][row1]+board[1][row1]+board[2][row1])
#         Rows.append(board[0][row2]+board[1][row2]+board[2][row2])
#
#         Rows.append(board[3][row0]+board[4][row0]+board[5][row0])
#         Rows.append(board[3][row1]+board[4][row1]+board[5][row1])
#         Rows.append(board[3][row2]+board[4][row2]+board[5][row2])
#
#         Rows.append(board[6][row0]+board[7][row0]+board[8][row0])
#         Rows.append(board[6][row1]+board[7][row1]+board[8][row1])
#         Rows.append(board[6][row2]+board[7][row2]+board[8][row2])
#
#         Cols=[]
#         Cols.append(board[0][col0]+board[3][col0]+board[6][col0])
#         Cols.append(board[0][col1]+board[3][col1]+board[6][col1])
#         Cols.append(board[0][col2]+board[3][col2]+board[6][col2])
#
#         Cols.append(board[1][col0]+board[4][col0]+board[7][col0])
#         Cols.append(board[1][col1]+board[4][col1]+board[7][col1])
#         Cols.append(board[1][col2]+board[4][col2]+board[7][col2])
#
#         Cols.append(board[2][col0]+board[5][col0]+board[8][col0])
#         Cols.append(board[2][col1]+board[5][col1]+board[8][col1])
#         Cols.append(board[2][col2]+board[5][col2]+board[8][col2])
#
#         def isvalid(l):
#             digits = set()
#             for c in l:
#                 if c != '.' and c in digits:
#                     return False
#                 digits.add(c)
#             return True
#
#         for i,r in enumerate(Rows):
#             if not isvalid(r):
#                 print "r",i
#                 return False
#         for i,c in enumerate(Cols):
#             if not isvalid(c):
#                 print "c",i
#                 return False
#         for i,b in enumerate(board):
#             if not isvalid(b):
#                 print "b",i
#                 return False
#         return True

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):

        for l in board:
            m = [0 for x in xrange(10)]
            for c in l:
                if c != '.':
                    m[int(c)] += 1
                    if m[int(c)] > 1:
                        return False

        for col in xrange(9):
            m = [0 for x in xrange(10)]
            for row in xrange(9):
                if board[row][col] != '.':
                    m[int(board[row][col])] += 1
                    if  m[int(board[row][col])] > 1:
                        return False
        for x in xrange(0,9,3):
            for y in xrange(0,9,3):
                m = [0 for z in xrange(10)]
                for i in xrange(3):
                    for j in xrange(3):
                        if board[x+i][y+j] != '.':
                            m[int(board[x+i][y+j])] += 1
                            if m[int(board[x+i][y+j])] > 1:
                                return False

        return True




b = 	["7...4....","...865...",".1.2.....",".....9...","....5.5..",".........","......2..",".........","........."]
so = Solution()
print so.isValidSudoku(b)