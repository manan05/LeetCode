class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def helper(index, curr):
            # base case:
            if index == n:
                res.append(curr[:])
                return
            # include the choice
            curr.append(nums[index])
            helper(index + 1, curr)

            # Exclude the choice
            curr.pop()
            helper(index + 1, curr)

        helper(0, [])
        return res
