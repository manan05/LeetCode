class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        
        n = len(nums1)
        if(n % 2 != 0):
            median = nums1[(0+n)//2]
        else:
            median = (nums1[n//2] + nums1[(n//2) - 1])/2
        return median