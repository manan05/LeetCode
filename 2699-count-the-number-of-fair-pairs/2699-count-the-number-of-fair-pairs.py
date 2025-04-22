class Solution:
    def checkTwoPointer(self, nums, value):
        left = 0
        right = len(nums) - 1
        res = 0
        while left < right:
            mSum = nums[left] + nums[right]
            if mSum < value:
                res += right - left
                left += 1
            else:
                right -= 1
        return res

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # # Approach 1: Binary search
        nums.sort()
        lower_res = self.checkTwoPointer(nums, lower)
        upper_res = self.checkTwoPointer(nums, upper + 1)
        return upper_res - lower_res