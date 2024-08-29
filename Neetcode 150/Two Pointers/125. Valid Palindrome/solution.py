class Solution:
    def checkPalindrome(s):
        lower_str = s.lower()
        cut_str = []
        for i in lower_str:
            if i.isalnum():
                cut_str.append(i)
        l = 0
        r = len(cut_str) - 1
        while l < r:
            if cut_str[l] != cut_str[r]:
                return False
            l += 1
            r -= 1
        return True


s = "A man, a plan, a canal: Panama"
print(Solution.checkPalindrome(s))
