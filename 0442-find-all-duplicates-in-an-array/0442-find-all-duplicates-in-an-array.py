class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        mSet = set()
        res = []
        for i in nums:
            if i in mSet:
                res.append(i)
            else:
                mSet.add(i)
        return res
