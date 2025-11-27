class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxCount = 0
        i = 0
        j = 0
        while j < len(s):
            if s[j] in seen:
                while s[j] in seen and i < len(s):
                    seen.remove(s[i])
                    i += 1
            maxCount = max(maxCount, j - i + 1)
            seen.add(s[j])
            j += 1
        return maxCount