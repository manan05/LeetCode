class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # # Approach 1: Brute Force
        # m = len(matrix)
        # n = len(matrix[0])
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == target:
        #             return True

        # return False

        # # Approach 2: Binary search
        m, n = len(matrix), len(matrix[0])
        left, right = 0, (m * n - 1)

        while (left <= right):
            pivot = (left + right) // 2
            elem = matrix[pivot // n][pivot % n]
            if target == elem:
                return True
            elif target > elem:
                left = pivot + 1
            else:
                right = pivot - 1
        return False
