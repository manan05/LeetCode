class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        count = Counter(nums)
        for key, val in count.items():
            if val == 2:
                res.append(key)
        return res
