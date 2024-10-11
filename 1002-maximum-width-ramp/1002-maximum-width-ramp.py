class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        myStack = []
        maxW = 0

        for i in range(n):
            if not myStack or nums[myStack[-1]] > nums[i]:
                myStack.append(i)
        for j in range(n - 1, -1, -1):
            while myStack and nums[myStack[-1]] <= nums[j]:
                maxW = max(maxW, j - myStack[-1])
                myStack.pop()

        return maxW


