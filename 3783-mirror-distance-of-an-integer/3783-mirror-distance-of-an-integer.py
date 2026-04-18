class Solution:
    def mirrorDistance(self, n: int) -> int:
        revNum = self.reverseN(n)
        print(revNum)
        print(abs(n - revNum))
        return abs(n - revNum)

    def reverseN(self, n):
        res = 0
        while n != 0:
            res = res * 10 + n % 10
            n = n // 10
        return res

# 25
# res = 0
# res = 0 + 5
# n = 2

# res = 50 + 2