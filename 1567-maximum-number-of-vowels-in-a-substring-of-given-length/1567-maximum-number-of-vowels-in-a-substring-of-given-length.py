class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        r = k -1
        n = len(s)
        ss = s[l:r+1]
        vowels = ['a', 'e', 'i', 'o', 'u']
        count = 0
        for i in ss:
            if i in vowels:
                count += 1
        maxCount = count
        r += 1
        while(r < n):
            if s[l] in vowels:
                count -= 1
            if s[r] in vowels:
                count += 1
            l += 1
            r += 1
            maxCount = max(maxCount, count)
        return maxCount