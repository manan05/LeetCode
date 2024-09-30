class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 2 pointer approach
        l, r = 0, 1 # L = buy, R= Sell
        maxP = 0
        while (r < len(prices)):
            if(prices[l] < prices[r]):
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
                r += 1
            else:
                l = r # because here we find a price that is lower and maximizes the profit
                r += 1
        return maxP
