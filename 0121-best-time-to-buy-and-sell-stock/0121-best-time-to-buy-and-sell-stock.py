class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Approach 1: Brute Force
        # maxP = 0
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         profit = prices[j] - prices[i]
        #         maxP = max(maxP, profit)
        # return maxP

        # Approach 2: DP
        currP = prices[0]
        maxP = 0
        for i in prices:
            currP = min(i , currP)
            maxP = max(maxP, i - currP)
        return maxP