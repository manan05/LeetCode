class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = 10 ** 9 + 7
        n = len(nums)
        count = 0
        left = 0
        right = n - 1
        while left <= right:
            if nums[left] + nums[right] <= target:
                count = (count + pow(2, (right - left), mod)) % mod
                left += 1
            else:
                right -= 1
        return count
