class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # # Approach 1: using Array for extra space
        # row = len(matrix)
        # col = len(matrix[0])
        # zeroes = []
        # for i in range(row):
        #     for j in range(col):
        #         if matrix[i][j] == 0:
        #             zeroes.append((i, j))
        # for x, y in zeroes:
        #     temp = 0
        #     while(temp != row):
        #         matrix[temp][y] = 0
        #         temp += 1
        #     temp = 0
        #     while(temp != col):
        #         matrix[x][temp] = 0
        #         temp += 1

        # # Approach 2: Using Set for extra space
        # m = len(matrix)
        # n = len(matrix[0])
        # rows = set()
        # cols = set()

        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             rows.add(i)
        #             cols.add(j)

        # for i in range(m):
        #     for j in range(n):
        #         if i in rows or j in cols:
        #             matrix[i][j] = 0

        # Approach 3 - Constant Space
        R = len(matrix)
        C = len(matrix[0])
        is_col = False
        for i in range(R):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, R):
            for j in range(1, C):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0

        if is_col == 1:
            for i in range(R):
                matrix[i][0] = 0
