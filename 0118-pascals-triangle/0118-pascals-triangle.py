class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Approach 1: DP
        res = []

        for i in range(numRows):
            row = [1 for _ in range(i + 1)]
            row[0], row[-1] = 1, 1
            for j in range(1, len(row) - 1):
                row[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(row)
        return res
