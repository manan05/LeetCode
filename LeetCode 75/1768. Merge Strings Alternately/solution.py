# problem link: https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75
# company tags: Uber

class solution:
    def mergeAlternatively(word1, word2):
        m = len(word1)
        n = len(word2)
        res = ""
        for i in range(min(m,n)):
            res += (word1[i])
            res += (word2[i])
        if(m> n):
            res += (word1[n:])
        else:
            res += (word2[m:])
        return res
        

word1 = str(input("Enter first word: "))
word2 = str(input("Enter second word: "))
print(solution.mergeAlternatively(word1, word2))