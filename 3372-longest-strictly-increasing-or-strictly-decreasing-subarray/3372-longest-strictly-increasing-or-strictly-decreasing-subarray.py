class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxA = 0
        
        for i in range(len(nums)):
            c = 1
            for j in range(i + 1, len(nums)):
                if(nums[j] < nums[j-1]):
                    c += 1
                else:
                    break
            maxA = max(c, maxA)
        
        for i in range(len(nums)):
            c = 1
            for j in range(i + 1, len(nums)):
                if(nums[j] > nums[j - 1]):
                    c += 1
                else:
                    break
            maxA = max(c, maxA)
        return maxA