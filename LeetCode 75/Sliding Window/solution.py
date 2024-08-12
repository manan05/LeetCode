# Question link: https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75

# Companies: Facebook


class Solution:
    def maxAvgSubArr(nums, k):
        i = 1
        maxSum = -1000000
        currSum = sum(nums[0:k])
        maxSum = max(maxSum, currSum)

        for j in range(k, len(nums)):
            currSum += nums[j] - nums[i - 1]
            maxSum = max(maxSum, currSum)
            i += 1
        return maxSum / k


nums = [1, 12, -5, -6, 50, 3]
k = 4
print(Solution.maxAvgSubArr(nums, k))
