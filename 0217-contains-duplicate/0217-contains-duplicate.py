class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mSet = set()
        for i in nums:
            if i in mSet:
                return True
            else:
                mSet.add(i)
        return False