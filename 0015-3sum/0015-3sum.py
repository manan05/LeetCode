class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, res, i)
        return res

    def twoSum(self, nums, res, i):
        seen = set()
        j = i + 1
        while j < len(nums):
            comp = 0 - nums[i] - nums[j]
            if comp in seen:
                res.append([nums[i], nums[j], comp])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1
