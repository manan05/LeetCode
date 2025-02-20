class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maxN = max(nums)
        minN = min(nums)
        for i in range(minN, 0, -1):
            if minN % i == 0 and maxN % i == 0:
                return i
        