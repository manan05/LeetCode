class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 1
        for i in range(len(word) - 1):
            for j in range(i + 1, len(word)):
                if word[i] == word[j]:
                    res += 1
                break
        return res
