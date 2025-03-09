class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # # Approach 1: constant space but sorting (O(nlogn)) this involves modifying too
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i-1] == nums[i]:
        #         return nums[i]

        # # Approach 2: Set approach, linear space
        # mySet = set()
        # for i in nums:
        #     if i in mySet:
        #         return i
        #     mySet.add(i)

        # # Approach 3: Negative Marking
        # for i in nums:
        #     curr = abs(i)
        #     if nums[curr] < 0:
        #         duplicate = curr
        #         break
        #     nums[curr] = - nums[curr]
        # for i in range(len(nums)):
        #     nums[i] = abs(nums[i])
        # return duplicate

        # # Approach 4: using extra space without modifying
        # hmap = {}
        # for i in range(len(nums)):
        #     if hmap.get(nums[i], 0) != 0:
        #         return nums[i]
        #     hmap[nums[i]] = 1

        # # Approach 5: without using extra space:
        low = 1
        high = len(nums) - 1
        while low <= high:
            curr = (low + high) // 2
            count = 0
            count = sum(num<= curr for num in nums)
            if count > curr:
                duplicate = curr
                high = curr - 1
            else:
                low = curr + 1
        return duplicate