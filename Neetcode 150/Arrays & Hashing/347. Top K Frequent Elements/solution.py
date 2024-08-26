# There are 3 ways in which we can solve this problem, with 3 different time complexities

# - 1st method is: 

from collections import Counter

class Solution:
    def topKFrequentNlogN(nums, k):
        frequency = Counter(nums)
        print(frequency)
        sorted_list = sorted(frequency, key = frequency.get, reverse=True)
        print(sorted_list)
        return sorted_list[:k]
        

nums = [1,1,1,2,2,3]
k = 2
print(Solution.topKFrequentNlogN(nums, k))