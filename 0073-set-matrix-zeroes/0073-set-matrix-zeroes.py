class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # # Approach 1: Using Arr of tuples to store
        # arr = []
        # m = len(matrix)
        # n = len(matrix[0])
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             arr.append((i, j))
        # for row, col in arr:
        #     for i in range(n):
        #         matrix[row][i] = 0
        #     for j in range(m):
        #         matrix[j][col] = 0

        # # Approach 2: Using Set
        # rows = set()
        # cols = set()
        # m = len(matrix)
        # n = len(matrix[0])
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             rows.add(i)
        #             cols.add(j)
        # for i in range(m):
        #     for j in range(n):
        #         if i in rows or j in cols:
        #             matrix[i][j] = 0

        is_col = False
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for i in range(n):
                matrix[0][i] = 0
        
        if is_col:
            for i in range(m):
                matrix[i][0] = 0