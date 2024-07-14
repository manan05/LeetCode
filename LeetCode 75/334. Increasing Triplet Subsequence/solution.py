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
    
    def incTripleSubsequenceOnWithoutSpace(arr):
        first = second = float('inf')
        first_idx = second_idx = -1

        for i in range(len(arr)):
            if(arr[i] <= first and i > first_idx):
                first = arr[i]
                first_idx = i
            elif(arr[i] <= second and i > second_idx):
                second = arr[i]
                second_idx = i
            else:
                return True
        return False
        

arr = [0,1,2,3,4]
print(Solution.incTripleSubsequenceOnWithoutSpace(arr))