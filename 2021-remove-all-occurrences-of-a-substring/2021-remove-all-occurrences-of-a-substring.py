class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # iteration
        while part in s:
            start = s.find(part)
            s = s[:start] + s[start + len(part):]
        return s