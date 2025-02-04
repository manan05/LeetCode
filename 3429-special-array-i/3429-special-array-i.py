class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        if (n == 1):
            return True
        for i in range(1, n):
            pf = 1  # assuming forward parity as 1 - Odd
            pb = 1  # assuming backward parity as 1 - Odd
            if (nums[i] % 2 == 0):
                pf = 0  # changing to even parity
            if (nums[i - 1] % 2 == 0):
                pb = 0  # changing to even parity
            if (pb == pf):
                return False
        return True
