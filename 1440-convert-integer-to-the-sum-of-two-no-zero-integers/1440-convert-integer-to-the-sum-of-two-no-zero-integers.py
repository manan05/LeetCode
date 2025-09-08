class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            res = []
            if '0' not in str(i):
                res.append(i)
                z = n - i
                if '0' not in str(z):
                    res.append(z)
                    return res
