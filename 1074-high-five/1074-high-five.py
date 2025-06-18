import heapq
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # # Sorting:
        # mapping = defaultdict(list)
        # items.sort(key=lambda x: (x[0], -x[1]))
        # for student, score in items:
        #     mapping[student].append(score)
        # res = []
        # for id in mapping:
        #     topFive = mapping[id][:5]
        #     res.append([id, sum(topFive) // 5])
        # return res

        # # Using Heap
        mapping = defaultdict(list)
        for student, score in items:
            heapq.heappush(mapping[student], score)
            if len(mapping[student]) > 5:
                heapq.heappop(mapping[student])

        res = []
        for id in mapping:
            res.append([id, sum(mapping[id]) // 5])
        return sorted(res)
