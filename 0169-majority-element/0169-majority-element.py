from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = {}
        c = Counter(nums)
        max_n = 0
        for i in c.values():
            max_n = max(max_n, i)
        for i,j in c.items():
            if j == max_n:
                return i
        