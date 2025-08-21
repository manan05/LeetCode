class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mSet = set()
        for num in nums:
            if num in mSet:
                return True
            else:
                mSet.add(num)
        return False
