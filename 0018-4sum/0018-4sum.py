class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quad = []
        res = []
        n = len(nums)
        nums.sort()

        def kSum(start, k, target):
            if k != 2:
                for i in range(start, n - k + 1):
                    if i > start and nums[i - 1] == nums[i]:
                        continue
                    quad.append(nums[i])
                    kSum(i + 1, k - 1, target - nums[i])
                    quad.pop()
                return
            l = start
            r = n - 1
            while l < r:
                currSum = nums[l] + nums[r]
                if currSum > target:
                    r -= 1
                elif currSum < target:
                    l += 1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
        kSum(0, 4, target)
        return res
