# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        minval = n
        while(left < right):
            mid = left + (right - left)//2
            val = isBadVersion(mid)
            if(val):
                minval = min(minval, mid)
                right = mid
            else:
                left = mid + 1
        return minval