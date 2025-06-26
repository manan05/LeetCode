class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for i in s:
            hashmap[i] = hashmap.get(i, 0) + 1
        for idx, ch in enumerate(s):
            if hashmap[ch] == 1:
                return idx
        return -1
