class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0
        maxOne = 0
        for i in nums:
            if i == 1:
                curr += 1
            else:
                maxOne = max(curr, maxOne)
                curr = 0
        return max(curr, maxOne)