class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # # Approach 1: Brute Force

        # res = []
        # for i in queries:
        #     nums[i[1]] += i[0]
        #     mySum = 0
        #     for j in nums:
        #         if j %2 == 0:
        #             mySum += j
        #     res.append(mySum)
        # return res

        # # Approach 2: Optimized
        arr_sum = sum(x for x in nums if x%2 == 0)
        res = []
        for x, k in queries:
            if nums[k] % 2 == 0:
                arr_sum -= nums[k]
            nums[k] += x
            if (nums[k] % 2 == 0):
                arr_sum += nums[k]
            
            res.append(arr_sum)
        return res
