class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if board[r][c] != "O":
                return

            board[r][c] = "T"
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        # 1. capture the unsrounded O next to the border mark it to "T"
        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == "O" and r in [0, rows-1] or c in [0, cols-1]):
                    dfs(r, c)

        # 2. mark the srounded O into X
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # 3. unmark the T to O agian
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"

        
                

                
            

