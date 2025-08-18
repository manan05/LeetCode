class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mdict = {}
        for s in strs:
            if tuple(sorted(s)) in mdict:
                mdict[tuple(sorted(s))].append(s)
            else:
                mdict[tuple(sorted(s))] = [s]
        return [x for x in mdict.values()]