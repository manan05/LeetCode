class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            newStr = s[:i] + s[i+1:]
            if(s[i] not in newStr):
                return i
        return -1