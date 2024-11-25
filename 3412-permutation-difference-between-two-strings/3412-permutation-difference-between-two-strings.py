class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        sHash = {}
        tHash = {}
        diff = 0
        n = len(s)
        for i in range(n):
            sHash[s[i]] = i
        for j in range(n):
            tHash[t[j]] = j
        for i in sHash.keys():
            diff += abs(sHash.get((i)) - tHash.get(i))
        return diff