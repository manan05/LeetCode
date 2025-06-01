class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    empty_cells.append((i, j))
                else:
                    rows[i].add(val)
                    cols[j].add(val)
                    box_idx = (i // 3) * 3 + (j // 3)
                    boxes[box_idx].add(val)

        def backtrack(index):
            if index == len(empty_cells):
                return True

            i, j = empty_cells[index]
            box_idx = (i // 3) * 3 + (j // 3)
            for num in range(1, 10):
                num = str(num)
                if num not in rows[i] and num not in cols[j] and num not in boxes[box_idx]:
                    board[i][j] = num
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box_idx].add(num)

                    if backtrack(index + 1):
                        return True

                    # Backtrack
                    board[i][j] = '.'
                    rows[i].remove(num)
                    cols[j].remove(num)
                    boxes[box_idx].remove(num)
            return False

        backtrack(0)
