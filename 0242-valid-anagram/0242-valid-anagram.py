class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # s = sorted(s)
        # t = sorted(t)
        # print(s, t)
        # i = 0
        # while i < len(s):
        #     if s[i] != t[i]:
        #         return False
        #     i += 1
        # return True
        counter = Counter(s)
        for ch in t:
            if ch not in counter:
                return False
            else:
                counter[ch] -= 1
        for i in counter.values():
            if i != 0:
                return False
        return True
