class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # # Approach 1: Brute Force
        # for i in range(n):
        #     nums1[m + i] = nums2[i]
        # nums1.sort()

        # # Approach 2: 
        tempArr = nums1[:m]

        p1 = 0
        p2 = 0

        p = 0
        while (p < m + n):
            if p2>= n or (p1 < m and (tempArr[p1] <= nums2[p2])):
                nums1[p] = tempArr[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2+= 1
            p += 1
        
