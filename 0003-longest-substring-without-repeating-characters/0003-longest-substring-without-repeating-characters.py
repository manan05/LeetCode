class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        resSet = set()
        l, maxLen = 0, 0

        for r in range(0, len(s)):
            while(s[r] in resSet):
                resSet.remove(s[l])
                l += 1
            resSet.add(s[r])
            maxLen = max(maxLen, (r-l+1))

        return maxLen
