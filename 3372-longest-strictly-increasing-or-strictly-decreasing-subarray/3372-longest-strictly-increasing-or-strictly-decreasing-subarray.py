class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # maxA = 0
        
        # for i in range(len(nums)):
        #     c = 1
        #     for j in range(i + 1, len(nums)):
        #         if(nums[j] < nums[j- 1]):
        #             c += 1
        #         else:
        #             break
        #     maxA = max(maxA, c)
        
        # for i in range(len(nums)):
        #     c = 1
        #     for j in range(i + 1, len(nums)):
        #         if(nums[j] > nums[j - 1]):
        #             c += 1
        #         else:
        #             break
        #     maxA = max(c, maxA)
        # return maxA

        if len(nums) == 1:
            return 1
        
        si = 1
        sd = 1
        maxA = 1
        for i in range(len(nums) - 1):
            if(nums[i] < nums[i + 1]):
                si += 1
                sd = 1
            elif (nums[i] > nums[i + 1]):
                sd += 1
                si = 1
            else:
                si = 1
                sd = 1
            maxA = max(maxA, si, sd)
        return maxA