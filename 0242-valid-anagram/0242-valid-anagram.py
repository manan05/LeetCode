from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = Counter(s)
        for i in t:
            if i in counter:
                counter[i] = counter[i] - 1
            else:
                return False
        for i in counter.values():
            if i != 0:
                return False
        return True