class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # res = []
        # arr.sort()
        # minDiff = float('inf')
        # n = len(arr)
        # for i in range(n - 1):
        #     currDiff = arr[i + 1] - arr[i]
        #     minDiff = min(minDiff, currDiff)
        # for i in range(n - 1):
        #     currDiff = arr[i + 1] - arr[i]
        #     if currDiff == minDiff:
        #         res.append([arr[i], arr[i + 1]])
        # return res

        # # Count sort approach
        min_val = min(arr)
        max_val = max(arr)

        offset = -min_val
        freq = [0] * (max_val - min_val + 1)

        for num in arr:
            freq[num + offset] = 1

        prev = None
        minDiff = float('inf')
        res = []
        for i in range(len(freq)):
            if freq[i] == 1:
                if prev is not None:
                    currDiff = i - prev
                    if currDiff < minDiff:
                        res = [[prev - offset, i - offset]]
                        minDiff = currDiff
                    elif currDiff == minDiff:
                        res.append([prev - offset, i - offset])
                prev = i
        return res
