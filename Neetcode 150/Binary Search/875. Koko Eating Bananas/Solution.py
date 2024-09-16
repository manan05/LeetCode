import math
class Solution:
    def minEatingSpeed(piles, h):
        left = 1
        right = max(piles)
        while(left < right):
            mid = (left + right)//2
            hours = 0
            for i in piles:
                hours = hours + math.ceil(i/mid)
            if(hours <= h):
                right = mid 
            else:
                left = mid + 1
        return left
                

                

piles, h= [3,6,7,11], 8
print(Solution.minEatingSpeed(piles=piles, h=h))