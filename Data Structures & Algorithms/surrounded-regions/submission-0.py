class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        def captureDfs(i, j):
            if (i < 0 or j < 0 or i >= ROWS or j >= COLS or \
                board[i][j] != 'O'
            ):
                return 
            board[i][j] = 'T'
            captureDfs(i + 1, j);
            captureDfs(i - 1, j);
            captureDfs(i, j + 1);
            captureDfs(i, j - 1);
        
        for row in range(ROWS) :
            if board[row][0] == 'O' :
                captureDfs(row, 0)
            if board[row][COLS - 1] == 'O' :
                captureDfs(row, COLS - 1)
        
        for col in range(COLS) :
            if board[0][col] == 'O':
                captureDfs(0, col)
            if board[ROWS - 1][col] == 'O':
                captureDfs(ROWS - 1, col)
        

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
        