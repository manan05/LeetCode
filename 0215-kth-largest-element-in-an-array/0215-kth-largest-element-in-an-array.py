import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # # Brute Force
        # nums.sort(reverse=True)
        # for i in range(len(nums)):
        #     if i == k - 1:
        #         return nums[i]

        # # Optimized (heap)
        res = []
        for i in range(len(nums)):
            heapq.heappush(res, nums[i])
            if i > k - 1:
                heapq.heappop(res)
        return res[0]
