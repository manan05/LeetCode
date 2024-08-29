from collections import defaultdict

# Condition: must write an algo that runs in O(n) time

class Solution:
    def longestConsecutive(nums):
        # create a set
        set_vals = set(nums)
        
        count = 0

        for i in nums:
            # check if start of a sequence
            if(i-1 not in set_vals):
                length = 0
                while(i + length) in set_vals:
                    length += 1
                count = max(count, length)
        return count



nums = [100,4,200,1,3,2]
nums2 = [0,3,7,2,5,8,4,6,0,1]
print(Solution.longestConsecutive(nums = nums))
print(Solution.longestConsecutive(nums= nums2))