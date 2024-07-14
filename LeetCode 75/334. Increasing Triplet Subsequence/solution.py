# Question Link: https://leetcode.com/problems/increasing-triplet-subsequence/description/?envType=study-plan-v2&envId=leetcode-75

# Companies: Google, Facebook

class Solution:
    def incTripletSubsequenceOn2(arr):
        test = []
        for i in range(len(arr)-2):
            for j in range(i,len(arr)-1):
                if(arr[i] < arr[j]):
                    test.append([i,j])
        for i in range(len(arr)):
            for j in test:
                if(i > j[1] and arr[i] > arr[j[1]]):
                    return True
        return False

        

arr = [1,5,0,4,1,3]
print(Solution.incTripletSubsequence(arr))