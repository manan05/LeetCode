class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # # Approach 1: Brute Force
        # maxC = 0
        # for i in nums:
        #     curr = i
        #     currC = 1
        #     while curr + 1 in nums:
        #         curr = curr + 1
        #         currC += 1
        #     maxC = max(maxC, currC)
        # return maxC

        # # Approach 2: Sorting
        # if not nums:
        #     return 0

        # nums.sort()
        # maxC = 1
        # currC = 1
        # for i in range(1, len(nums)):
        #     if nums[i] != nums[i - 1]:
        #         if nums[i] - nums[i - 1] == 1:
        #             currC += 1
        #         else:
        #             maxC = max(maxC, currC)
        #             currC = 1
        # maxC = max(maxC, currC)
        # return maxC

        # # Approach 3: Set
        if not nums:
            return 0
        mySet = set(nums)
        maxC = 1
        for i in mySet:
            if i - 1 not in mySet:
                currNum = i
                currC = 1
                while currNum + 1 in mySet:
                    currNum = currNum + 1
                    currC += 1
                maxC = max(maxC, currC)
        return maxC
