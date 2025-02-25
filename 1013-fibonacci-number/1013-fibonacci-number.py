class Solution:
    def fib(self, n: int) -> int:
        # base case
        if n == 1 or n == 0:
            return n

        fibnm1 = self.fib(n - 1)
        fibnm2 = self.fib(n - 2)

        return fibnm1 + fibnm2
