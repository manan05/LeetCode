class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # # Naive solution
        # for i in nums2:
        #     nums1.append(i)
        # nums1.sort()
        
        # n = len(nums1)
        # if(n % 2 != 0):
        #     median = nums1[(0+n)//2]
        # else:
        #     median = (nums1[n//2] + nums1[(n//2) - 1])/2
        # return median

        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total //2

        if (len(B) < len(A)):
            A,B = B,A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r)//2 # A
            j = half - i - 2 # B, j = index so we subtract 2

            leftA = A[i] if i >= 0 else float("-infinity")
            rightA = A[i + 1] if i + 1 < len(A) else float("infinity")

            leftB = B[j] if j >= 0 else float("-infinity")
            rightB = B[j + 1] if j + 1 < len(B) else float("infinity")
        
            # partition correct
            if(leftA <= rightB and leftB<=rightA):
                # odd
                if total % 2 != 0:
                    return min(rightA, rightB)
                # even
                
                return (max(leftA, leftB) + min(rightA, rightB)) /2
            elif (leftA > rightB):
                r = i - 1
            else:
                l = i + 1

