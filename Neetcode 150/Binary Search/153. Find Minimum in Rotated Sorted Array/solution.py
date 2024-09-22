class Solution:
    def findMin(nums):
        if(len(nums)) == 1:
            return nums[0]
        
        left = 0
        right = len(nums) - 1

        # no rotation
        if(nums[0] < nums[right]):
            return nums[0]
        
        while right>= left:
            mid = left + (right - left)//2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # mid - 1 > mid
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            if nums[mid] > nums[0]:
                left = mid + 1
            
            else:
                right = mid - 1

nums = [11,13,15,17]
print(Solution.findMin(nums = nums))