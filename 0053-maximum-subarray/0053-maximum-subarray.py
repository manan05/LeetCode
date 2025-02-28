class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # # Approach 1: O(n3)
        # if len(nums) == 1:
        #     return nums[0]
        # maxSum = - math.inf
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         maxSum = max(maxSum, sum(nums[i:j+1]))
        # return maxSum

        # # Approach 2: O (N2) Optimized Brute Force
        # maxSum = -math.inf
        # for i in range(len(nums)):
        #     curr_sum = 0
        #     for j in range(i, len(nums)):
        #         curr_sum += nums[j]
        #         maxSum = max(curr_sum, maxSum)
        # return maxSum

        # # Approach 3: Kadane Algo : O(N) - Linear
        maxSum = nums[0]
        currSum = nums[0]
        for i in range(1, len(nums)):
            currSum = max(nums[i], currSum + nums[i])
            maxSum = max(maxSum, currSum)
        return maxSum