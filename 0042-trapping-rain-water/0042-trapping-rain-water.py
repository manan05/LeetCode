class Solution:
    def trap(self, height: List[int]) -> int:
        # # Brute Force:
        # ans = 0
        # n = len(height)
        # for i in range(1, n - 1):
        #     left_max = 0
        #     right_max = 0
        #     for j in range(i, -1, -1):
        #         left_max = max(left_max, height[j])
        #     for j in range(i, n):
        #         right_max = max(right_max, height[j])
        #     ans += min(left_max, right_max) - height[i]
        # return ans    

        # # Approach 2: DP
        # ans = 0
        # n = len(height)
        # left_max = [0] * n
        # right_max = [0] * n

        # left_max[0] = height[0]
        # for i in range(1, n):
        #     left_max[i] = max(height[i], left_max[i - 1])

        # right_max[n - 1] = height[n - 1]
        # for i in range(n - 2, -1, -1):
        #     right_max[i] = max(height[i], right_max[i + 1])

        # for i in range(1, n - 1):
        #     ans += min(left_max[i], right_max[i]) - height[i]

        # return ans

        # # Approach 3: Two Pointer Approach
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
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
