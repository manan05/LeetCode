class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # brute force using space
        # hashmap = {}
        # for i in nums:
        #     hashmap[i] = hashmap.get(i, 0) + 1
        # p0 = hashmap.get(0,0)
        # p1 = p0 + hashmap.get(1, 0)

        # for i in range(len(nums)):
        #     if i < p0:
        #         nums[i] = 0
        #     elif (i >= p0 and i < p1):
        #         nums[i] = 1
        #     else:
        #         nums[i] = 2


        # 3 pointer approach
        curr = 0
        p0 = 0
        p2 = len(nums) - 1
        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                curr += 1
                p0 += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1
                