class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mSet = set(nums)
        maxCount = 0
        for num in mSet:
            if num - 1 not in mSet:
                currNum = num
                currCount = 1
                while currNum + 1 in mSet:
                    currNum += 1
                    currCount += 1
                maxCount = max(currCount, maxCount)
        return maxCount