# must write an algorithm that runs in O(N) without using the division operator

class Solution:
    def productOfArrayExceptSelf(nums):
        ans = [1 for x in nums]

        pre = 1
        for i in range(len(nums)):
            ans[i] = ans[i] * pre
            pre = pre * nums[i]

        post = 1
        for j in range(len(nums)-1, -1, -1):
            ans[j] = ans[j] * post
            post = post * nums[j]

        return ans

nums = [1,2,3,4]
print(Solution.productOfArrayExceptSelf(nums))