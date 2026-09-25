class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check that no duplicate values in rows, cols, and squares
        # return False if duplicate found

        # Square check:
        for i in range(3):
            for j in range(3):
                square = []
                for x in range(i*3, i*3+3):
                    for y in range(j*3, j*3+3):
                        if board[x][y] != '.':
                            if board[x][y] in square:
                                return False
                            square.append(board[x][y])
        
        # Row check:
        for row in board:
            cur = []
            for n in row:
                if n != '.':
                    if n in cur: return False
                    cur.append(n)
        
        # Col check:
        for i in range(9):
            cur = []
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] in cur: return False
                    cur.append(board[j][i])

        return True


                
