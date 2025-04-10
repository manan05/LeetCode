class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # # Approach 1: Sorting
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i-1] == nums[i]:
        #         return nums[i]

        # # Approach 2: Using Set
        # mySet = set()
        # for i in nums:
        #     if i in mySet:
        #         return i
        #     else:
        #         mySet.add(i)

        # # Approach 3: Using Hashmap
        # myDict = {}
        # for i in nums:
        #     if myDict.get(i, 0) == 1:
        #         return i
        #     else:
        #         myDict[i] = 1

        # # Approach 4: Modified Binary search
        # low = 1
        # high = len(nums) - 1

        # while low <= high:
        #     mid = (low + high) // 2
        #     count = 0

        #     for i in nums:
        #         if i <= mid:
        #             count += 1

        #     if count > mid:
        #         duplicate = mid
        #         high = mid - 1
        #     else:
        #         low = mid + 1

        # return duplicate

        # # Approach 5: Optimized: Slow and Fast pointer

        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow