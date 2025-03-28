class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        temp_arr = [0] * n
        for i in range(n):
            temp_arr[(i + k) % n] = nums[i]
        nums[:] = temp_arr
