class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        maxNum = -1
        for key, freq in counter.items():
            if key == freq:
                maxNum = max(maxNum, key)
        return maxNum
