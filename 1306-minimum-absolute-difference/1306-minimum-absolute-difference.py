class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        res = []
        arr.sort()
        minDiff = float('inf')
        n = len(arr)
        for i in range(n - 1):
            currDiff = arr[i + 1] - arr[i]
            minDiff = min(minDiff, currDiff)
        for i in range(n - 1):
            currDiff = arr[i + 1] - arr[i]
            if currDiff == minDiff:
                res.append([arr[i], arr[i + 1]])
        return res
