class Solution:
    def mySqrt(self, x: int) -> int:

        if (x == 0 or x == 1) :
            return x
        l = 1
        r = x // 2
        while (l <= r):
            mid = l+(r-l)//2
            sq = mid * mid
            if(sq == x):
                return mid
            elif(sq > x):
                r = mid - 1
            else:
                l = mid + 1
        return r