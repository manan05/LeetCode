class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # # Kadanes (DP)
        currSum = nums[0]
        maxSum = nums[0]
        for i in nums[1:]:
            currSum = max(i, currSum + i)
            maxSum = max(maxSum, currSum)
        return maxSum