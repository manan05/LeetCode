class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        maxCount = 0
        for num in unique:
            if num - 1 not in unique:
                nxt = num + 1
                currC = 1
                while nxt in unique:
                    nxt += 1
                    currC += 1
                maxCount = max(currC, maxCount)
        return maxCount