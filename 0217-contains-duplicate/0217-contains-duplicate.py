class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # # Brute Force Solution # # Sorting
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i - 1] == nums[i]:
        #         return True
        # return False

        mSet = set(nums)
        if len(mSet) != len(nums):
            return True
        return False
