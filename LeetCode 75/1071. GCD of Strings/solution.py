# Question Link : https://leetcode.com/problems/greatest-common-divisor-of-strings/?envType=study-plan-v2&envId=leetcode-75

# Company: Goldman Sachs, Atlassian

class Solution:
    def GCDofStrings(str1, str2):
        m = len(str1)
        n = len(str2)
        for i in range(min(m,n), 0, -1):
            if(m%i == 0 and n % i == 0):
                b1 = m //i
                b2 = n // i
                if(str1[:i] * b2 == str2) and (str2[:i] * b1 == str1):
                    return str2[:i]
        return ""

ip1 = str(input())
ip2 = str(input())
print(Solution.GCDofStrings(ip1, ip2)) 

