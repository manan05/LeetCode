class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_str = s.lower()
        cut_str = ""
        for i in lower_str:
            if i.isalnum():
                cut_str += i
        left = 0
        right = len(cut_str) - 1
        while left < right:
            if cut_str[left] != cut_str[right]:
                return False
            left += 1
            right -= 1
        return True
