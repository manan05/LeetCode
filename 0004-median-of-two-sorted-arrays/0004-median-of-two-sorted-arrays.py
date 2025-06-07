class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        id1 = (n + m) // 2
        id2 = id1 - 1
        i = 0
        j = 0
        p = 0
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                if p == id1:
                    id1_elem = nums1[i]
                if p == id2:
                    id2_elem = nums1[i]
                p += 1
                i += 1
            else:
                if p == id1:
                    id1_elem = nums2[j]
                if p == id2:
                    id2_elem = nums2[j]
                p += 1
                j += 1

        while i < n:
            if p == id1:
                id1_elem = nums1[i]
            if p == id2:
                id2_elem = nums1[i]
            p += 1
            i += 1
        while j < m:
            if p == id1:
                id1_elem = nums2[j]
            if p == id2:
                id2_elem = nums2[j]
            p += 1
            j += 1
        if (n + m) % 2 != 0:
            return id1_elem
        else:
            return (id1_elem + id2_elem) / 2