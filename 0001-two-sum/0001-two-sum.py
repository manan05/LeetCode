class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap and hashmap[diff] != i:
                return [i, hashmap[diff]]
            hashmap[nums[i]] = i
        return -1
