
# There are 3 ways in which we can solve this problem, with 3 different time complexities

# - 1st method is: creating a counter called frequency and then sorting the frequency and key as frequency.get and reverse sort. then return using slicing

# we can also use min heap for this where heapify is logN and we are doing it k times so it becomes KlogN

# BUT we can solve this question in O(n) using bucket sort

class Solution:
    def topKFrequentNlogN(nums, k):
        frequency = Counter(nums)
        print(frequency)
        sorted_list = sorted(frequency, key = frequency.get, reverse=True)
        print(sorted_list)
        return sorted_list[:k]
    
    def topKFrequentON(nums, k):
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] =  1 + count.get(n, 0)
        
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) -1 , 0, -1):
            for n in freq[i]:
                res.append(n)
                if(len(res) == k):
                    return res

nums = [1,1,1,2,2,3]
k = 2
# print(Solution.topKFrequentNlogN(nums, k))
print(Solution.topKFrequentON(nums, k))
