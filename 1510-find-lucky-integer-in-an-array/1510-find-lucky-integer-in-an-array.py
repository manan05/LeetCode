class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        keys = sorted(counter.keys(), reverse=True)
        for i in keys:
            if counter[i] == i:
                return i
        return -1