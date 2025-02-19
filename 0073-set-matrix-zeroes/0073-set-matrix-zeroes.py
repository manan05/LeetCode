class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        zeroes = []
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    zeroes.append((i, j))
        for x, y in zeroes:
            temp = 0
            while(temp != row):
                matrix[temp][y] = 0
                temp += 1
            temp = 0
            while(temp != col):
                matrix[x][temp] = 0
                temp += 1