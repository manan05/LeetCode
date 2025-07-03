class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, 0, 0]
        for num in nums:
            temp = dp[:]
            for i in range(3):
                new_sum = temp[i] + num
                dp[new_sum % 3] = max(dp[new_sum % 3], new_sum)
        
        return dp[0]

        # n = len(nums)

        # def dp(i, mod):
        #     if i == n:
        #         return 0 if mod == 0 else float('-inf')
            
        #     skip = dp(i + 1, mod)

        #     take = nums[i] + dp(i + 1, (nums[i] + mod) % 3)

        #     return max(skip, take)

        # return dp(0, 0)