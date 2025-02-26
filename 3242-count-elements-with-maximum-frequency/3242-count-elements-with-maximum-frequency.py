from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        maxVal = max(c.values())
        res = 0
        for i in c.values():
            if i == maxVal:
                res += 1
        return res * maxVal