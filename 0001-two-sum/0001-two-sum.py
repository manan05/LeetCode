class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # Approach 1: Brute Force - 2 loops
        # for i in range(len(nums) - 1):
        #     for j in range(1, len(nums)):
        #         if (nums[i] + nums[j]) == target:
        #             return [i, j]

        # # Approach 2: 2 pass Hashmaps
        # myDict = {}
        # for i in range(len(nums)):
        #     myDict[nums[i]] = i 

        # for i in range(len(nums)):
        #     complement = target - nums[i]
        #     if complement in myDict and myDict[complement] != i:
        #         return [i, myDict[complement]]

        # # Approach 3: 1 pass Hashmap
        myDict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in myDict and myDict[complement] != i:
                return [i, myDict[complement]]
            else:
                myDict[nums[i]] = i