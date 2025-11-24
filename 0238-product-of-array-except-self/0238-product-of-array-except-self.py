class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_arr = [1] * (n + 1)
        post_arr = [1] * (n + 1)
        res = [1] * n
        for i in range(n):
            pre_arr[i + 1] = pre_arr[i] * nums[i]

        for i in range(n - 1, -1, -1):
            post_arr[i] = post_arr[i + 1] * nums[i]

        for i in range(n):
            res[i] = pre_arr[i] * post_arr[i + 1]

        return res
