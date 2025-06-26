import heapq
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        hashmap = defaultdict(list)
        for st, marks in items:
            heappush(hashmap[st], marks)
            if len(hashmap[st]) > 5:
                heappop(hashmap[st])
        res = []
        for st, marks in hashmap.items():
            res.append([st, sum(marks) // 5])
        return sorted(res)