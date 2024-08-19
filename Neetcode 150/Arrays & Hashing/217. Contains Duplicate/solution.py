# Question Link: https://leetcode.com/problems/contains-duplicate/description/
# Companies:  Amazon ✯   Adobe ✯   Google ✯   Apple ✯   Microsoft ✯   Bloomberg   Uber   Yahoo   tcs  

class Solution:
    def containsDuplicateN2(nums):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if(nums[i] == nums[j]):
                    return True
        return False
    
    def containsDuplicateNLogN(nums):
        list.sort(nums)

        for i in range(len(nums) -1):
            if( nums[i] == nums[i+1]):
                return True
        return False
    
    def containsDuplicateN(nums):
        
        mySet = set()
        for i in range(len(nums)):
            if(nums[i] not in mySet):
                mySet.add(nums[i])
            else:
                return True
        return False

    

nums = [1,1,1,3,3,4,3,2,4,2]
# print(Solution.containsDuplicateN2(nums))
print(Solution.containsDuplicateNLogN(nums))