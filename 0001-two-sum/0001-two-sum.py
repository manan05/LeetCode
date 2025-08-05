class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hmap:
                return [i, hmap[complement]]
            hmap[nums[i]] = i
