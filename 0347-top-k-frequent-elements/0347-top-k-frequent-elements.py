import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counter = Counter(nums)
        min_heap = []
        for elem, count in counter.items():
            heapq.heappush(min_heap, (count, elem))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        for c, elem in min_heap:
            res.append(elem)
        return res
