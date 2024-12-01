class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while(l<=r):
            mid = (l + r) //2
            check = nums[mid]
            if(check == target):
                return mid
            elif(check > target):
                r = mid - 1
            else:
                l = mid + 1
        return mid + 1 if (mid +1 == l) else mid