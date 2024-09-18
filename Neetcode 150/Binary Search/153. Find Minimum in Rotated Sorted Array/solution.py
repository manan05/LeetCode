class Solution:
    def findMin(nums):
        l = 0
        r = len(nums) - 1

        # base condition
        if len(nums) == 1:
            return nums[0]
        
        # if no rotation
        if(nums[l] < nums[r]):
            return nums[l]

        while (r >= l):
            mid = l+ (r-l)//2
            elem = nums[mid]

            if(nums[mid+1] < elem):
                return nums[mid +1]
            if (nums[mid-1] > elem):
                return elem
            if(nums[mid] > nums[l]):
                l = mid +1
            else:
                r = mid -1
    



nums = [11,13,15,17]
print(Solution.findMin(nums = nums))