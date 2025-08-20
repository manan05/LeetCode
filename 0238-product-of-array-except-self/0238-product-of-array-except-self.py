class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1 for _ in range(n)]
        pre = 1
        for i in range(n):
            res[i] = pre * res[i]
            pre = pre * nums[i]
        post = 1
        for j in range(n - 1, - 1, -1):
            res[j] = post * res[j]
            post = post * nums[j]
        return res