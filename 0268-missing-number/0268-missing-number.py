
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # # Naive Solution (O(N Log N))
        # nums.sort()
        # for i in range(len(nums)):
        #     if i != nums[i]:
        #         return i
        # return i + 1

        # # HashMap (O (N))
        # myDict = {}
        # for i in range(len(nums)):
        #     myDict[nums[i]] = 1
        # for i in range(len(myDict)):
        #     if myDict.get(i) == None:
        #         return i
        # return i + 1

        # # Math Solution with O(1) - constant space
        n = len(nums)
        prod = (n*(n+1))//2
        mySum = 0
        for i in nums:
            mySum += i
        return prod - mySum
