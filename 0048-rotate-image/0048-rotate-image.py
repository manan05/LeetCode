class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # # Brute force - Which uses space  
        # n = len(matrix)
        # res = [[0 for _ in range(n)] for _ in range(n)]
        
        # for i in range(n):
        #     for j in range(n):
        #         res[j][n - 1 - i] = matrix[i][j]
        # print(res)

        # # Optimal Approach  - In Place - Transpose -> Reverse Row
        # transpose
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse
        for i in matrix:
            i.reverse()