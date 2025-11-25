class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ''
        for i in s:
            if i.isalnum():
                st += i.lower()
        l = 0
        r = len(st) - 1
        while l < r:
            if st[l] == st[r]:
                r -= 1
                l += 1
            else:
                return False
        return True
