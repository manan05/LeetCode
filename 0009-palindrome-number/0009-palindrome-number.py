class Solution:
    def isPalindrome(self, x: int) -> bool:
        revNum = 0
        temp = x
        while temp > 0:
            q = temp%10
            revNum = revNum*10 + q
            temp = temp//10
        if(revNum == x):
            return True
        else:
            return False