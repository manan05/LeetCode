class Solution:
    def clearDigits(self, s: str) -> str:
        res = []
        if s[0].isalpha():
            res.append(s[0])
        for i in range(1, len(s)):
            if s[i].isnumeric():
                res.pop()
            else:
                res.append(s[i])
        return "".join(res)