class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for st in strs:
            if tuple(sorted(st)) in hmap:
                hmap[tuple(sorted(st))].append(st)
            else:
                hmap[tuple(sorted(st))] = [st]
        return [x for x in hmap.values()]