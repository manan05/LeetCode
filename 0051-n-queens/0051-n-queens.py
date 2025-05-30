class Solution:
    def isSafe1(self, row, col, board, n):
        tempRow = row
        tempCol = col
        # # upper left diagonal
        while row >= 0 and col >= 0:
            if board[row][col] == 'Q':
                return False
            row -= 1
            col -= 1

        # # same row - left side
        row = tempRow
        col = tempCol
        while col >= 0:
            if board[row][col] == 'Q':
                return False
            col -= 1

        # # bottom left diagonal
        row = tempRow
        col = tempCol
        while row < n and col >= 0:
            if board[row][col] == 'Q':
                return False
            row += 1
            col -= 1

        return True

    def solve(self, col, board, res, n):
        if col == n:
            res.append(board[:])
            return
        
        for row in range(n):
            if self.isSafe1(row, col, board, n):
                board[row] = board[row][:col] + 'Q' + board[row][col + 1:]
                self.solve(col + 1, board, res, n)
                board[row] = board[row][:col] + '.' + board[row][col + 1:]

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = ["." * n for _ in range(n)]
        res = []
        self.solve(0, board, res, n)
        return res