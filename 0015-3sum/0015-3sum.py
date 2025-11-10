class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                if threeSum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < n and nums[left - 1] == nums[left]:
                        left += 1
                elif threeSum > 0:
                    right -= 1
                else:
                    left += 1
        return res
