class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = []
        for i in range(n):
            arr.append(nums[nums[i]])
        return arr
