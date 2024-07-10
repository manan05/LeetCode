# Question Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75

# Company: Amazon

class KidWithCandies:
    def solution(candies, extraCandies):
        res = []
        for i in candies:
            if((i + extraCandies) >= max(candies)):
                res.append(True)
            else:
                res.append(False)
        return res

print("Size of list:")
n = int(input())
candies = []
for i in range(n):
    candies.append(int(input()))
print("ExtraCandies?")
extraCandies = int(input())
print(KidWithCandies.solution(candies, extraCandies))
