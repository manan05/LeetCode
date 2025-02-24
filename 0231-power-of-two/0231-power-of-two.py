class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # # Recursive
        # if n == 1:
        #     return True
        # elif (n > 1 and n < 2) or n == 0:
        #     return False

        # # self work
        # next = n / 2

        # return self.isPowerOfTwo(next)

        # # O(1) Constant time
        if n == 0 or n < 0:
            return False

        logval = int(math.log10(n)/math.log10(2))
        if n == 2 ** logval:
            return True
        return False

        