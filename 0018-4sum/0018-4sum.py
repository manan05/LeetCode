class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quad = []
        res = []

        def kSum(start, k, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    quad.append(nums[i])
                    kSum(i + 1, k - 1, target - nums[i])
                    quad.pop()
                return
            l = start
            r = len(nums) - 1
            while l < r:
                currSum = nums[l] + nums[r]
                if currSum < target:
                    l += 1
                elif currSum > target:
                    r -= 1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        kSum(0, 4, target)
        return res
