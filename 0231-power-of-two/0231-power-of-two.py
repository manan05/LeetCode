class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        elif (n > 1 and n < 2) or n == 0:
            return False

        # self work
        next = n / 2

        return self.isPowerOfTwo(next)

        