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

    def maxKSumPairsLinear(nums, k):
        num_map = {}  # create an empty dictionary
        count = 0

        for num in nums:
            res = k - num
            if res in num_map and num_map[res] > 0:
                count += 1
                num_map[res] -= 1
            else:
                num_map[num] = num_map.get(res, 0) + 1

        return count

        print(dict)


nums = [3, 1, 3, 4, 3]
k = 6
# print(Solution.maxKSumPairs(nums, k))
print(Solution.maxKSumPairsLinear(nums, k))
