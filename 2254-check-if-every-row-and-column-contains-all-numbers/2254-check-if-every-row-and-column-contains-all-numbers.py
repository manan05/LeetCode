class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        # # checking rows
        for i in range(n):
            seen = [False] * n
            for j in range(m):
                idx = matrix[i][j] - 1
                if seen[idx] == False:
                    seen[idx] = True
                else:
                    return False
        
        # # Checking Cols
        for i in range(n):
            seen = [False] * n
            for j in range(m):
                idx = matrix[j][i] - 1
                if (seen[idx] == False):
                    seen[idx] = True
                else:
                    return False
            
        return True