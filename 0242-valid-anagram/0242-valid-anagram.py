class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = Counter(s)
        for i in t:
            counter[i] = counter.get(i, 0) - 1
        for j in counter.values():
            if j != 0:
                return False
        return True
