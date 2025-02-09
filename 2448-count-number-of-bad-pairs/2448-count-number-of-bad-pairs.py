class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total_pairs = (n * (n-1))//2
        myDict = {}

        for i in range(n):
            diff = nums[i] - i
            myDict[diff] = myDict.get(diff, 0) + 1
        good_count = 0
        for y in myDict.values():
            if (y > 1):
                good_count += (y * (y - 1)) // 2

        return total_pairs - good_count