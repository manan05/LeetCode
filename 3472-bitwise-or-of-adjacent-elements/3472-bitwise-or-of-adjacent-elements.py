class Solution:
    def orArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0] * (n - 1)
        for i in range(n - 1):
            arr[i] = nums[i] | nums[i+1]
        return arr