class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        while(j<len(nums)):
            if(nums[i] != nums[j]):
                i = j
                j += 1
            else:
                nums.pop(j)

        return len(nums)