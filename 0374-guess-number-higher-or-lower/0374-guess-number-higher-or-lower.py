# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 0
        high = n
        
        while(low <= high):
            mid = low + (high - low)//2
            ans = guess(mid)
            if(ans == 0):
                return mid
            elif(ans == -1):
                high = mid -1
            elif(ans == 1):
                low = mid + 1