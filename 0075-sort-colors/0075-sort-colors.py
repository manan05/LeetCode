class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # O(N)
        # countZero = 0
        # countOne = 0
        # countTwo = 0

        # for i in nums:
        #     if i == 0:
        #         countZero += 1
        #     elif i == 1:
        #         countOne += 1
        #     else:
        #         countTwo += 1

        # for i in range(countZero):
        #     nums[i] = 0
        # for i in range(countOne):
        #     nums[i + countZero] = 1
        # for i in range(countTwo):
        #     nums[i + (countZero + countOne)] = 2

        # # One Pass with constant memory

        p0 = curr = 0
        p2 = len(nums) - 1

        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                curr += 1
                p0 += 1
            elif nums[curr] == 2:
                nums[p2], nums[curr] = nums[curr], nums[p2]
                p2 -= 1
            else:
                curr += 1
