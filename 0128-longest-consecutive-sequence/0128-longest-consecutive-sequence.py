class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        maxCount = 0
        for num in unique:
            if num - 1 not in unique:
                nxt = num + 1
                currCount = 1
                while nxt in unique:
                    currCount += 1
                    nxt += 1
                maxCount = max(maxCount, currCount)
        return maxCount
