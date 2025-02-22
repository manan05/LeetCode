import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # # Mathematical Solution O(1)
        # if n <= 0:
        #     return False
        # res = math.log10(n) / math.log10(3)
        # if(3 ** int(res)) != n:
        #     return False
        # return True

        # # Recursive Solution
        if n == 3.0 or n == 1:
            return True
        if n < 1 or (n > 1 and n < 2):
            return False
        
        return self.isPowerOfThree(n/3)
