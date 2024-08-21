class Solution:
    def twoSum(nums, target):
        dict = {}
        # building the HashMap for INDEX
        for i in range(len(nums)):
            dict[nums[i]] = i
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if(diff in dict and dict[diff] != i):
                return [i, dict[diff]]
        return []


nums = [3,3]
target = 6
print(Solution.twoSum(nums= nums, target=target))