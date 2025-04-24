class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        k = len(set(nums))
        res = 0

        for i in range(len(nums)):
            mSet = set()
            for j in range(i, len(nums)):
                mSet.add(nums[j])
                if len(mSet) == k:
                    res += 1
        return res
