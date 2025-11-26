class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = -float('inf')
        minPrice = float('inf')
        for price in prices:
            minPrice = min(minPrice, price)
            maxPro = max(maxPro, price - minPrice)
        return maxPro
