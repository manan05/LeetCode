class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        bought = 0
        for i in costs:
            if coins == 0:
                return bought
            if coins >= i:
                coins -= i
                bought += 1
            else:
                break
        return bought
