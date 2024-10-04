from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        HashMap = Counter(nums)
        maxCount = 0
        
        for key in HashMap.keys():
            count = 0
            if(HashMap[key +1]):
                count += HashMap.get(key) + HashMap.get(key + 1)
            maxCount = max(maxCount, count)
        return maxCount