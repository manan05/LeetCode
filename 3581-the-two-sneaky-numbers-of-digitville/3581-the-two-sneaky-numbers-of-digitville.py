class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        mSet = set()
        for i in nums:
            if i in mSet:
                res.append(i)
            else:
                mSet.add(i)
        return res
