class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def elementSum(val):
            temp = val
            s = 0
            while(temp != 0):
                s += temp % 10
                temp = temp // 10
            return s
        
        sum_pairs = []
        for num in nums:
            s = elementSum(num)
            sum_pairs.append((s, num))
        sum_pairs.sort()
        
        # checking both current and previous is same sum
        maxSum = -1
        for i in range(1, len(sum_pairs)):
            curr_sum = sum_pairs[i][0]
            prev_sum = sum_pairs[i - 1][0]

            if (curr_sum == prev_sum):
                maxSum = max(maxSum, (sum_pairs[i][1] + sum_pairs[i - 1][1]))
        return maxSum