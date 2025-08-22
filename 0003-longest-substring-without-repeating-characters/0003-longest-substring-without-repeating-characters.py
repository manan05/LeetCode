class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        i, j = 0, 0
        maxCount = 0
        while i < len(s) and j < len(s):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            maxCount = max(maxCount, (j - i + 1))
            j += 1
        return maxCount