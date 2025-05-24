class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        def helper(index, curr):
            if index == n:
                res.append(curr[:])
                return

            # include
            curr.append(nums[index])
            helper(index + 1, curr)


            # Exclude
            curr.pop()
            next_idx = index + 1
            while next_idx < n and nums[index] == nums[next_idx]:
                next_idx += 1
            helper(next_idx, curr)

        helper(0, [])
        return res
