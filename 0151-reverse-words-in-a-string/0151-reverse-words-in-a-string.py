class Solution:
    def reverseWords(self, s: str) -> str:
        res = s.split()
        i, j = 0, len(res) - 1
        while i < j:
            res[i], res[j] = res[j], res[i]
            i += 1
            j -= 1
        return " ".join(res)
