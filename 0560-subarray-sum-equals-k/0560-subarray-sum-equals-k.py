class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # # Brute Force, O(n^3)
        # res = []
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         if sum(nums[i:j + 1]) == k:
        #             res.append(nums[i : j + 1])
        # return len(res)

        # # Optimized O(n^2) - but still TLE
        # res = 0
        # currSum = 0
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         currSum += nums[j]
        #         if currSum == k:
        #             res += 1
        #     currSum = 0

        # return res

        # # Optimized
        hashmap = defaultdict(int)
        hashmap[0] = 1
        currSum = 0
        count = 0
        for num in nums:
            currSum += num
            if (currSum - k) in hashmap:
                count += hashmap[currSum - k]
            hashmap[currSum] += 1
        return count