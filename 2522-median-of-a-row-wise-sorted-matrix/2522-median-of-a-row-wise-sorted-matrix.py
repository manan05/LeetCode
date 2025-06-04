import bisect
class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        def calcSmaller(grid, mid):
            ans = 0
            for i in range(m):
                ans += bisect_right(grid[i], mid)
            return ans

        m = len(grid)
        n = len(grid[0])
        low = min([grid[i][0] for i in range(m)])
        high = max([grid[i][n - 1] for i in range(m)])
        while low <= high:
            mid = (low + high) // 2
            smallerEquals = calcSmaller(grid, mid)
            if smallerEquals <= (n * m) // 2:
                low = mid + 1
            else:
                high = mid - 1
        return low
