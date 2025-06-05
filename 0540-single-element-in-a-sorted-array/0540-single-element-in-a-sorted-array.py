class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid + 1] == nums[mid]:
                if mid % 2 == 0:
                    low = mid + 2
                else:
                    high = mid - 1
            elif nums[mid - 1] == nums[mid]:
                if mid % 2 == 0:
                    high = mid - 2
                else:
                    low = mid + 1
            else:
                return nums[mid]
        return nums[low]