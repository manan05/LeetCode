class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        maxS = 0
        for i in range(n):
            sum1 = nums[i]
            for j in range(i + 1, n):
                if(nums[j] > nums[j-1]):
                    sum1 += nums[j]
                else:
                    break
            maxS = max(maxS, sum1)
        
        return maxS