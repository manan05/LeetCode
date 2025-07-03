class Solution:
    def trap(self, height: List[int]) -> int:
        # # Brute Force
        # ans = 0
        # for i in range(1, len(height) - 1):
        #     left_max = 0
        #     right_max = 0
        #     for j in range(i, -1, -1):
        #         left_max = max(left_max, height[j])
        #     for j in range(i, len(height)):
        #         right_max = max(right_max, height[j])
        #     ans += min(left_max, right_max) - height[i]
        # return ans

        # # Optimized Solution
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        ans = 0
        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                ans += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                ans += right_max - height[right]
                right -= 1
        return ans

