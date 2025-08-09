import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        min_heap = []
        for key, count in counter.items():
            heappush(min_heap, (count, key))
            if len(min_heap) > k:
                heappop(min_heap)
        return [y for x, y in min_heap]
