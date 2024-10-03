class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        counter = {}
        maxWindow = 0

        for r in range(n):
            counter[s[r]] = counter.get(s[r], 0) + 1
            while (r - l + 1) - max(counter.values()) > k:
                # not valid ss
                counter[s[l]] -= 1
                l += 1
            maxWindow = max(maxWindow, r - l + 1)
        return maxWindow
