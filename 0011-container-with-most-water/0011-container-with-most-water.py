class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA = 0
        l = 0
        r = len(height) - 1
        while l < r:
            currA = (r - l) * min(height[l], height[r])
            maxA = max(currA, maxA)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return maxA
