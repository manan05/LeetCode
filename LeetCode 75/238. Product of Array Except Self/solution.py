# Question link: https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75

# Company: Amazon, Facebook, Microsoft, Asana, Apple, Uber, Adobe, Bloomberg, Oracle
# must write an algo that runs O(n) without division operation

class Solution:
    # O(n square)
    def productExceptSelfOn2(a):
        ans = [1 for x in a]
        for i in range(len(a)):
            prod = 1
            for j in range(len(a)):
                if (i != j):
                    prod = prod * a[j]
            ans[i] = prod
        return ans   

    # O(n) but with space as O(N)
    def productExceptSelf(a):
        ans = [1 for x in a]
        pre = a.copy()
        post = a.copy()
        for i in range(1, len(a)):
            pre[i] = pre[i-1] * a[i]
        for i in range(len(a)-2, -1, -1):
            post[i] = post[i+1] * a[i]

        ans[0] = 1* post[1]
        ans[len(ans)-1] = pre[len(ans)-2] *1
        for i in range(1,len(a)-1):
            ans[i] = pre[i-1] * post[i+1]
        return ans
    
    def productExceptSelfOP(a):
        ans = [1 for x in a]
        
        pre = 1
        for i in range(len(a)):
            ans[i] *= pre
            pre *= a[i]

        post = 1
        for j in range(len(a)-1, -1,-1):
            ans[j] *= post
            post *= a[j]

        return ans

 
a = []
n = int(input())
for i in range(n):
    a.append(int(input()))

# print(Solution.productExceptSelfOn2(a))
# print(Solution.productExceptSelf(a))
print(Solution.productExceptSelfOP(a))
