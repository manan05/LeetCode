import math
class Solution:
    def containerWithMostWater(height):
        left = 0
        right = len(height) - 1
        maxArea = 0
        while(left < right):
            newArea = ((right - left) * (min(height[left], height[right])))
            maxArea = max(maxArea, newArea)
            if(height[left] >= height[right]):
                right -= 1
            else:
                left += 1
        return maxArea




height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution.containerWithMostWater(height))
