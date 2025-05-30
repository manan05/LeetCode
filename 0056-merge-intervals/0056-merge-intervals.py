class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        for interval in intervals:
            if res and res[-1][1] >= interval[0]:
                if res[-1][1] < interval[1]:
                    res[-1][1] = interval[1]
            else:
                res.append(interval)
        return res