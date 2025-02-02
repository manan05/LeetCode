class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        resA = []
        res = 0
        for i in digits:
            res = res*10 + i
        res += 1
        temp = res
        while(temp > 0):
            resA.append(temp%10)
            temp = temp//10
        resA.reverse()
        return (resA)