class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxSum = 0
        for i in accounts:
            temp = sum(i)
            maxSum = max(maxSum, temp)
        return maxSum