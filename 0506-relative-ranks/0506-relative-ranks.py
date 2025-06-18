import heapq
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        res = []
        for index, point in enumerate(score):
            heapq.heappush(res, (-point, index))
        ans = [0] * len(score)
        place = 1
        while res:
            og_idx = heapq.heappop(res)[1]
            if place == 1:
                ans[og_idx] = "Gold Medal"
            elif place == 2:
                ans[og_idx] = "Silver Medal"
            elif place == 3:
                ans[og_idx] = "Bronze Medal"
            else:
                ans[og_idx] = str(place)
            place += 1
        return ans
