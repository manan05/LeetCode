class Solution:
    def secondHighest(self, s: str) -> int:
        res = set()
        for i in s:
            if i.isdigit():
                res.add(i)
        res = sorted(res)   # O(1)
        return int(res[-2]) if len(res) >= 2 else -1
