class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while (k > 0):
            lowest = nums.index(min(nums))
            nums[lowest] *= multiplier
            k -= 1
        return nums
