class Solution:
    def scoreOfString(self, s: str) -> int:
        arr = [ord(ch) for ch in s]
        res = 0
        for i in range(len(arr) - 1):
            res += abs(arr[i] - arr[i + 1])
        return res