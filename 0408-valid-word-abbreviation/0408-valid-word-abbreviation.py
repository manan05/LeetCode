class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j] == '0':
                return False
            elif abbr[j].isdigit():
                k = j
                while k < len(abbr) and abbr[k].isdigit():
                    k += 1
                i += int(abbr[j: k])
                j = k
            else:
                return False
        if i == len(word) and j == len(abbr):
            return True
        return False
