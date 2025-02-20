class Solution:
    def isArmstrong(self, n: int) -> bool:
        num_str = str(n)
        k = len(num_str)
        res = 0
        for i in num_str:
            res += int(i) ** k
        return res == n