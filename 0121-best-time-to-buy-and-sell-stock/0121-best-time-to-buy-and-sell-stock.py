class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    #    # Approach 1: Brute Force:

    #     maxP = 0
    #     for i in range(len(prices) - 1):
    #         for j in range(i + 1, len(prices)):
    #             profit = prices[j] - prices[i]
    #             maxP = max(profit, maxP)
    #     return maxP

    # # Approach 2: One Pass Algo

        curr = prices[0]
        maxP = 0
        for i in range(1, len(prices)):
            curr = min(prices[i], curr)
            maxP = max(prices[i] - curr, maxP)
        return maxP