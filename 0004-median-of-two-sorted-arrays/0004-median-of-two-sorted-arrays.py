class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # # Approach 1: Linear TC
        # n, m = len(nums1), len(nums2)
        # id1 = (n + m) // 2
        # id2 = id1 - 1
        # i = 0
        # j = 0
        # p = 0
        # while i < n and j < m:
        #     if nums1[i] < nums2[j]:
        #         if p == id1:
        #             id1_elem = nums1[i]
        #         if p == id2:
        #             id2_elem = nums1[i]
        #         p += 1
        #         i += 1
        #     else:
        #         if p == id1:
        #             id1_elem = nums2[j]
        #         if p == id2:
        #             id2_elem = nums2[j]
        #         p += 1
        #         j += 1

        # while i < n:
        #     if p == id1:
        #         id1_elem = nums1[i]
        #     if p == id2:
        #         id2_elem = nums1[i]
        #     p += 1
        #     i += 1
        # while j < m:
        #     if p == id1:
        #         id1_elem = nums2[j]
        #     if p == id2:
        #         id2_elem = nums2[j]
        #     p += 1
        #     j += 1
        # if (n + m) % 2 != 0:
        #     return id1_elem
        # else:
        #     return (id1_elem + id2_elem) / 2

        # # Approach 2: Logarithmic TC
        n1 = len(nums1)
        n2 = len(nums2)
        n = n1 + n2
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        low = 0
        high = n1
        left = (n + 1) // 2

        while low <= high:
            mid1 = (low + high) // 2
            mid2 = left - mid1
            l1, l2, r1, r2 = float('-inf'), float('-inf'), float('inf'), float('inf')
            if mid1 < n1:
                r1 = nums1[mid1]
            if mid2 < n2:
                r2 = nums2[mid2]
            if mid1 - 1 >= 0:
                l1 = nums1[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = nums2[mid2 - 1]
            if l1 <= r2 and l2 <= r1:
                if n % 2 != 0:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
