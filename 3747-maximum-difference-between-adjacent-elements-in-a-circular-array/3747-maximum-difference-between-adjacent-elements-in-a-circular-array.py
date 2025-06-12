class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        maxDiff = abs(nums[0] - nums[-1])
        for i in range(1, len(nums)):
            diff = abs(nums[i] - nums[i - 1])
            maxDiff = max(diff, maxDiff)
        return maxDiff
