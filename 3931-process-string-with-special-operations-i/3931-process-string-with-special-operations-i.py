class Solution:
    def processStr(self, s: str) -> str:
        res = []
        for i in s:
            if i == '*':
                if res:
                    del res[-1]
            elif i == '#':
                a = res
                res.extend(a)
            elif i == '%':
                res.reverse()
            else:
                res.append(i)
        return "".join(res)
