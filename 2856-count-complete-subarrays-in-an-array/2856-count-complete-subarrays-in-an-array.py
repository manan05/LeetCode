class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # # Brute Force Solution
        # k = len(set(nums))
        # res = 0

        # for i in range(len(nums)):
        #     mSet = set()
        #     for j in range(i, len(nums)):
        #         mSet.add(nums[j])
        #         if len(mSet) == k:
        #             res += 1
        # return res

        # # Sliding Window approach
        k = len(set(nums))
        res = 0
        left = 0
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
            while len(hashmap) == k:
                res += len(nums) - i
                hashmap[nums[left]] = hashmap.get(nums[left]) - 1
                if hashmap[nums[left]] == 0:
                    del hashmap[nums[left]]
                left += 1
        return res


"""
Brute Force Solution: O(N^2):
    - Logic: iterate so that you can get all the subarrays and then just check if len(set) == k

Optimized: Sliding Window
    - left = 0, res = 0, k found out using len of set
    - map banaya, counted the occurences of the elements, once size of map == k:
    - res me add kardiya till the end of loop
    - left waale element ki frequency kam kari from map and left increase kardiya 
        if frequency == 0 ho gayi then just deleted the element
"""