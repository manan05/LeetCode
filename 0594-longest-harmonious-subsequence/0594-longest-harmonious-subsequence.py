class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # # Using sorting (ONlogN)
        # counter = Counter(nums)
        # nums.sort()
        # maxL = 0
        # for i in range(1, len(nums)):
        #     if nums[i] - nums[i - 1] == 1:
        #         maxL = max(maxL, counter[nums[i]] + counter[nums[i - 1]])
        # return maxL

        # # Using only Hashmap
        counter = Counter(nums)
        maxL = 0
        for key in counter.keys():
            if key + 1 in counter:
                maxL = max(maxL, counter[key + 1] + counter[key])
        return maxL
