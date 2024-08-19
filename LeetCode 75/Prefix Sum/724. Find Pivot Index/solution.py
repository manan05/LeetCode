# Question Link: https://leetcode.com/problems/find-pivot-index/description/?envType=study-plan-v2&envId=leetcode-75
# Companies:  Facebook ✯   Goldman Sachs ✯   Apple ✯   Amazon ✯   Google ✯   Microsoft   Cisco   Expedia   Adobe  

class Solution:
    def findPivot(nums):
        lsum = [0]
        totalSum = sum(nums)

        for i in range(1, len(nums)):
            lsum.append(nums[i-1] + lsum[i-1])
        # print(lsum)

        for i in range(len(nums)):
            left = lsum[i]
            right = totalSum - left - nums[i]

            if(left == right):
                return i
        return -1

nums = [1,7,3,6,5,6]
print(Solution.findPivot(nums))