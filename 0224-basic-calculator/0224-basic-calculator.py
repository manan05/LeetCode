class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        sign = 1 # +1 for + and -1 for -
        i = 0
        stack = []
        while i < len(s):
            if s[i].isdigit():
                k = i
                while k < len(s) and s[k].isdigit():
                    k += 1
                num = int(s[i: k])
                res = res + (sign * num)
                i = k
                continue
            if s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == '(':
                stack.append((res, sign))
                res = 0
                sign = 1
            elif s[i] == ')':
                old_res, old_sign = stack.pop()
                res = old_res + (res * old_sign)
            i += 1
        return res
