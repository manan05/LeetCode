# Question link : https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75
# Companies: Amazon


# O(N Log N) solution
class Solution:
    def maxKSumPairs(nums, k):
        count = 0
        i, j = 0, len(nums) - 1
        while i < j:
            sum = nums[i] + nums[j]
            if sum == k:
                count += 1
                i += 1
                j -= 1
            elif sum > k:
                j -= 1
            else:
                i += 1
        return count


nums = [3, 1, 3, 4, 3]
k = 6
print(Solution.maxKSumPairs(nums, k))
