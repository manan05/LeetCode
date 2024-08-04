# Question link: https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75

# Company: Bloomberg


class Solution:
    def reverseVowels(s):
        arr = list(s)
        i = 0
        j = len(s) - 1
        vowels = ['a', 'e', "i", "o", "u"]
        while i < j:
            if arr[i].lower() in vowels:
                if arr[j].lower() in vowels:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    j -= 1
                else:
                    j -= 1
            else:
                i += 1
        return "".join(arr)


s = input()
print(Solution.reverseVowels(s))
