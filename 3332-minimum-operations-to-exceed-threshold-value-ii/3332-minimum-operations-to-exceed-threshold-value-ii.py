import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        counter = 0
        while nums[0] < k:
            counter += 1
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            temp = (min(x, y) * 2 + max(x, y))
            heapq.heappush(nums, temp)
        return counter
