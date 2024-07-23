# Question Link: https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=leetcode-75
# Companies:  Amazon ✯   Microsoft ✯   Adobe ✯   Facebook ✯   Google ✯   Apple   Bloomberg   Swiggy   Goldman Sachs  

class Solution:
    def mostWater(arr):
        i, j = 0, len(arr) -1
        maxArea = 0
        while(i<j):
            newArea = abs((j-i) * min(arr[j], arr[i]))
            if(newArea > maxArea):
                maxArea = newArea
            if(arr[i] > arr[j]):
                j -= 1
            else:
                i += 1
        return maxArea

arr = [1,8,6,2,5,4,8,3,7]
print(Solution.mostWater(arr))