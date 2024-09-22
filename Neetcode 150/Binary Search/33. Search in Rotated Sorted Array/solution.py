class Solution:
    def searchRotatedArr(nums):
        left  = 0
        right = len(nums) - 1
        if(nums[0] < nums[right]):
            return nums[0]
        while(left <= right):
            mid = left + (right - left) // 2
            if(nums[mid] > nums[mid + 1]):
                return nums[mid + 1]
            if(nums[mid] > nums[right]):
                left = mid + 1
            else:
                right = mid - 1
        return -1
            
arr = [3,4,5,1,2]
print(Solution.searchRotatedArr(arr))


nums = [4,5,6,7,0,1,2]
target = 0