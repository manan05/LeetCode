class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        maxA = 0
        while i < j:
            currA = (j - i) * min(height[i], height[j])
            maxA = max(maxA, currA)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return maxA