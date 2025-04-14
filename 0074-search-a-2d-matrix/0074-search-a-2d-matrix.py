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
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = (m * n) - 1
        
        while (left <= right):
            pivot_idx = (left + right) // 2
            pivot_elem = matrix[pivot_idx // n][pivot_idx % n]
            if target == pivot_elem:
                return True
            else:
                if target > pivot_elem:
                    left = pivot_idx + 1
                else:
                    right = pivot_idx - 1
        return False