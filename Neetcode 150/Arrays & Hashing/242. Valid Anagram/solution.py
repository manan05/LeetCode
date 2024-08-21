class Solution:
    def isAnagram(s, t):
        dict = {}
        for i in s:
            if(i not in dict):
                dict[i] = 1
            else:
                dict[i] = dict.get(i) + 1
        
        for i in t:
            if(i not in dict):
                return False
            else:
                dict[i] = dict.get(i) - 1
        
        for i in dict.values():
            if(i != 0):
                return False
        return True
            

s = "anagram"
t = "nagaram"

print(Solution.isAnagram(s,t))