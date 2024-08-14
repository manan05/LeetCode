# Question link: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/?envType=study-plan-v2&envId=leetcode-75
# Companies: Amazon

class Solution:
    def maxVowelsSolutionON2(s, k):
        i = 0
        j = k-1
        maxCount = 0
        while(j< len(s)):
            count = 0
            for k in s[i: j+1]:
                if(k == 'a' or k == 'e' or k == 'i' or k == 'o' or k == 'u'):
                    count += 1
            maxCount = max(count, maxCount)
            i += 1
            j += 1
        return maxCount

    def maxVowelsSolutionSliding(s,k):
        i = 0
        j = k -1
        count = 0
        for z in s[i:j+1]:
            if (z == 'a' or z == 'e' or z == 'i' or z == 'o' or z == 'u'):
                count += 1
        maxCount = count
        i = 1
        j = k
        while(j < len(s)):
            if(s[i-1] == 'a' or s[i-1] == 'e' or s[i-1] == 'i' or s[i-1] == 'o' or s[i-1] == 'u'):
                count = count -1
            if(s[j]== 'a' or s[j] == 'e' or s[j] == 'i' or s[j] == 'o' or s[j] == 'u'):
                count = count + 1
            maxCount = max(maxCount, count)
            i += 1
            j += 1
        return maxCount



s = "abciiidef"
k = 3
print(Solution.maxVowelsSolutionSliding(s, k))