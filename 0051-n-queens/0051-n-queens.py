class Solution:
    def solve2(self, col, board, res, n, columns, diagonals, adiagonals):
        if col == n:
            res.append(board[:])
            return

        for row in range(n):
            curr_diag = row - col
            curr_anti_diag = row + col

            # placing queen safe or not
            if (row in columns) or (curr_diag in diagonals) or (curr_anti_diag in adiagonals):
                continue
            # place queen
            columns.add(row)
            diagonals.add(curr_diag)
            adiagonals.add(curr_anti_diag)
            board[row] = board[row][:col] + 'Q' + board[row][col + 1:]

            self.solve2(col + 1, board, res, n, columns, diagonals, adiagonals)
            # remove queen
            columns.remove(row)
            diagonals.remove(curr_diag)
            adiagonals.remove(curr_anti_diag)
            board[row] = board[row][:col] + '.' + board[row][col + 1:]


    def solveNQueens(self, n: int) -> List[List[str]]:
        board = ["." * n for _ in range(n)]
        res = []
        self.solve2(0, board, res, n, set(), set(), set())
        return res
