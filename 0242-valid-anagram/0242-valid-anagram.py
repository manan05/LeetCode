from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter_s = Counter(s)
        for i in t:
            if i in counter_s:
                counter_s[i] -= 1
            else:
                return False
        for val in counter_s.values():
            if val != 0:
                return False
        return True
