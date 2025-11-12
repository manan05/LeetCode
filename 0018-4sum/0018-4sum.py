class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def kSum(nums, target, k):
            res = []

            # check if no nums left
            if not nums:
                return res

            # greater than and less than avg check for 1st and last
            avg = target // k
            if nums[0] > avg or nums[-1] < avg:
                return res

            if k == 2:
                return twoSum(nums, target)

            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:  # duplicate check
                    for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
                        res.append([nums[i]] + subset)

            return res

        def twoSum(nums, target):
            res = []
            low, high = 0, len(nums) - 1
            while low < high:
                curr_sum = nums[low] + nums[high]
                if curr_sum < target or (low > 0 and nums[low - 1] == nums[low]):
                    low += 1
                elif curr_sum > target or (high < len(nums) - 1 and nums[high + 1] == nums[high]):
                    high -= 1
                else:
                    res.append([nums[low], nums[high]])
                    low += 1
                    high -= 1
            return res

        nums.sort()
        return kSum(nums, target, 4)
