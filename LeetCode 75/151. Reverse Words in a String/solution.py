# https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75

# Companies: Microsoft, Apple, LinkedIn, Amazon, Google, Visa

class Solution:
    def reverseWordsString(s):
        return " ".join(s.split()[::-1])

s = input()
print(Solution.reverseWordsString(s))