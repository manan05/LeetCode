class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        maxLen = 0
        left = 0
        for right in range(len(s)):
            # 2 cases
            # while s[right] in set or not in it
            while s[right] in hashset:
                hashset.remove(s[left])
                left += 1

            hashset.add(s[right])
            maxLen = max(maxLen, right - left + 1)

        return maxLen
