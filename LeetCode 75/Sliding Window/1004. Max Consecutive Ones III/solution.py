# Question Link: https://leetcode.com/problems/max-consecutive-ones-iii/description/?envType=study-plan-v2&envId=leetcode-75
# Companies: Facebook, Microsoft, Google, Amazon, ByteDance, Apple, Bloomberg


class Solution:
    def maxConsecutiveOnes(nums, k):
        i = 0
        j = -1
        maxSize = 0
        zeroCount = 0

        while i < len(nums):
            if nums[i] == 0:
                zeroCount += 1
                i += 1
            else:
                i += 1

            while zeroCount > k:
                j += 1
                if nums[j] == 0:
                    zeroCount -= 1

            maxSize = max((i - j - 1), maxSize)
        return maxSize


nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
k = 3

print(Solution.maxConsecutiveOnes(nums, k))
