class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # O(N) - Linear solution
        # for num in arr:
        #     if (num <= k):
        #         k += 1
        #     elif (num > k):
        #         break
        # return k

        # because sorted, binary search!!
        # O(logN)
        left = 0
        right = len(arr) - 1
        while (left <= right):
            pivot = (left + right) // 2
            if(arr[pivot] - pivot - 1 < k):
                left = pivot + 1
            else:
                right = pivot - 1
        
        return left + k

        
        
