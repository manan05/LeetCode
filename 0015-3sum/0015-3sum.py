class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    mSum = nums[i] + nums[left] + nums[right]
                    if mSum < 0:
                        left += 1
                    elif mSum > 0:
                        right -= 1
                    else:
                        res.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
        return res
