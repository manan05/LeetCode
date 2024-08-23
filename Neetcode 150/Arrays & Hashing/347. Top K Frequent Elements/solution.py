from collections import Counter

class Solution:
    def topKFrequent(nums, k):
        dict= Counter(nums)
        for i in dict.values():
            print(i)
        

nums = [1,1,1,2,2,3,4,4,4,4]
k = 2
print(Solution.topKFrequent(nums, k))