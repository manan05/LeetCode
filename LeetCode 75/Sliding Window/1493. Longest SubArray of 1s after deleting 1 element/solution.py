# question link: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/?envType=study-plan-v2&envId=leetcode-75

# Companies:Yandex, Amazon

class Solution:
    def longestSubarray(nums):
        i = 0
        j = -1
        count = 0
        maxCount = 0
        while i < len(nums):
            if nums[i] == 1:
                i += 1
            else:
                count += 1
                i += 1
            while(count >1):
                j += 1
                if(nums[j] == 0):
                    count -= 1
            
            maxCount = max(maxCount, (i -j -1))
        return maxCount -1


nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
print(Solution.longestSubarray(nums))
