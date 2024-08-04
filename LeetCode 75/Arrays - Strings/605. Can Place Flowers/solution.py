# Question Link: https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75

#Companies:  LinkedIn ✯   Facebook ✯   Amazon ✯   Bloomberg ✯   Yahoo ✯  

class Solution:
    def placeFlowers(flowerbed, n):
        count = 0
        for i in range(len(flowerbed)):
            if(flowerbed[i] == 0):
                if(len(flowerbed) == 1):
                    count += 1
                elif(i == 0):
                    if(flowerbed[i+1] == 0):
                        flowerbed[i] = 1
                        count += 1
                elif(i == len(flowerbed)-1):
                    if(flowerbed[i-1] == 0):
                        flowerbed[i] = 1
                        count += 1
                elif(flowerbed[i-1] == 0 and flowerbed[i+1] == 0):
                    flowerbed[i] = 1
                    count += 1
        if(count >= n):
            return True
        else:
            return False

print("Size of array:")
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
print("Plants to place:")
plants: int = int(input())
print(Solution.placeFlowers(arr, plants))
