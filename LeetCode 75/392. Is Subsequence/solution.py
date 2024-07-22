# Question link : https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=leetcode-75
# Companies name:  Amazon ✯   Bloomberg ✯   Facebook ✯   Microsoft ✯   Pinterest ✯   Zoho   Accolite   Tesco   PayTM   Quadrical AI   Google   Rootstock Software   Unthinkable Solutions   Josh Technologies   Yandex   Adobe


class Solution:
    def isSubsequence(s, t):
        i, j = 0,0
        while i < len(s) and j < len(t):
            if s[i] == s[j]:
                i += 1
                j += 1
            else:
                j += 1
        if(i == len(s)):
            return True
        else:
            return False

s = "abc"
t = "ahbgdc"
print(Solution.isSubsequence(s, t))
