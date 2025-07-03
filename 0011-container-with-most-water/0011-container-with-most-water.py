class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA = 0
        low = 0
        high = len(height) - 1
        while low <= high:
            currA = ((high - low) * min(height[low], height[high]))
            maxA = max(currA, maxA)
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        return maxA
