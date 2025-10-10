class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for st in strs:
            char = tuple(sorted(st))
            if char in hashmap:
                hashmap[char].append(st)
            else:
                hashmap[char] = [st]
        return [x for x in hashmap.values()]