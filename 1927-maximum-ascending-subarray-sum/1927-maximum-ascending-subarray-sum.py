class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # # Brute Force
        # n = len(nums)
        # maxS = 0
        # for i in range(n):
        #     sum1 = nums[i]
        #     for j in range(i + 1, n):
        #         if(nums[j] > nums[j-1]):
        #             sum1 += nums[j]
        #         else:
        #             break
        #     maxS = max(maxS, sum1)
        
        # return maxS

        # Linear Scan
        maxS = 0
        sum1 = nums[0]
        n = len(nums)
        for i in range(1, n):
            if(nums[i] <= nums[i-1]):
                maxS = max(maxS, sum1)
                sum1 = 0
            sum1 += nums[i]
        maxS = max(maxS, sum1)
        return maxS


