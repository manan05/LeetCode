class Solution:
    def moveZeroes(arr):
        if(len(arr) == 1):
            return
        i = 0
        j = 1
        while(i<j and j<len(arr)):
            if(arr[i] == 0):
                if(arr[j] != 0):
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    j += 1
                else:
                    j += 1
            else:
                i+=1
                j += 1


arr = [0,1,0,3,12]
print(Solution.moveZeroes(arr))
print(arr)