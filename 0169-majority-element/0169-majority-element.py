import random
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # # Approach 1: Hashmap
        # myDict = {}
        # for i in nums:
        #     myDict[i] = myDict.get(i, 0) + 1
        # print(myDict)
        
        # for i in myDict.items():
        #     if i[1] > len(nums) // 2:
        #         return i[0]

        # # Approach 2: Sorting
        # nums.sort()
        # # majority element > n/2 
        # return nums[len(nums) // 2]

        # # Approach 3: Randomization
        # while True:
        #     candidate = random.choice(nums)
        #     if sum(1 for elem in nums if elem == candidate) > len(nums) // 2:
        #         return candidate

        count = 0
        candidate = None

        for i in nums:
            if count == 0:
                candidate = i
            if i == candidate:
                count += 1
            else:
                count -= 1
        return candidate