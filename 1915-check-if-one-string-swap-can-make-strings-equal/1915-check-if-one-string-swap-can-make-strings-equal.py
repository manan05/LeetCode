from collections import Counter
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c = 0
        s1_dict = Counter(s1)
        s2_dict = Counter(s2)
        for i in s1_dict.keys():
            if(s2_dict[i] != s1_dict[i]):
                return False
        for i in range(len(s1)):
            if s1[i]!= s2[i]:
                c += 1
        return True if c==0 or c == 2 else False
