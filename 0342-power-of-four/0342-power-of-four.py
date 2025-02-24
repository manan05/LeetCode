class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # # Recursive Solution
        # # base case
        # if n == 1:
        #     return True
        # if (n > 1 and n < 2) or n <= 0:
        #     return False

        # # self work
        # next = n / 4

        # return self.isPowerOfFour(next)

        # # O(1) Constant time solution

        if n <= 0:
            return False

        logval = int(math.log10(n) / math.log10(4))

        if n == 4 ** logval:
            return True
        return False