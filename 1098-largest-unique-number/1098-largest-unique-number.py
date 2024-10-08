class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1
        for i in sorted(hashmap.keys())[::-1]:
            if(hashmap.get(i) == 1):
                return i
            else:
                continue
        return -1