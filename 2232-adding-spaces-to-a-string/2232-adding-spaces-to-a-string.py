class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        i = 0
        j = 0
        res = ""
        while(i < len(s) and j <len(spaces)):
            if(spaces[j] != i):
                res += s[i]
                i += 1
            else:
                res += ' '
                j += 1
                res += s[i]
                i += 1
        return res + s[i:]