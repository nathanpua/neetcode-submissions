class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.found = False

        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != word[i]:
                return
            if i == len(word) - 1:
                self.found = True
                return
            # ith character found, replace it with '#'
            char = word[i]
            board[r][c] = '#'
            dfs(r+1, c, i+1)
            dfs(r-1, c, i+1)
            dfs(r, c+1, i+1)
            dfs(r, c-1, i+1)
            board[r][c] = char
            
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, 0)

        return self.found