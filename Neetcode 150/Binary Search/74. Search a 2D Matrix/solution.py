class Solution:
    def searchMatrixNaive(matrix, target):
        rows = len(matrix)
        columns = len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == target:
                    return True
        return False

    def searchMatrixBinary(matrix, target):
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, (rows * cols) - 1  # first and last element

        while left <= right:
            mid = (left + right) // 2
            row = mid // cols
            col = mid % cols
            elem = matrix[row][col]

            if elem == target:
                return True
            elif elem > target:
                right = mid - 1
            else:
                left = mid + 1
        return False

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3

# print(Solution.searchMatrixNaive(matrix=matrix, target=target))
print(Solution.searchMatrixBinary(matrix=matrix, target=target))
