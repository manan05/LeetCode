class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def helper(curr):
            if len(curr) == n:
                res.append(curr[:])
                return

            for i in nums:
                if i not in curr:
                    curr.append(i)
                    helper(curr)
                    curr.pop()
        helper([])
        return res
