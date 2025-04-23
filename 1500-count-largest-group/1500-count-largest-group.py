class Solution:
    def countLargestGroup(self, n: int) -> int:
        hashmap = {}
        for i in range(1, n + 1):
            temp_sum = self.sumOfDigits(i)
            if temp_sum in hashmap:
                hashmap[temp_sum] = hashmap.get(temp_sum) + 1
            else:
                hashmap[temp_sum] = 1
        count = 0
        maxSum = max(hashmap.values())
        for i in hashmap.keys():
            if hashmap[i] == maxSum:
                count += 1
        return count


    def sumOfDigits(self, num):
        temp = num
        mSum = 0
        while temp != 0:
            mSum += temp % 10
            temp = temp // 10
        return mSum