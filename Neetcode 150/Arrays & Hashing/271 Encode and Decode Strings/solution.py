class Solution:

    def encode(strs):
        res = ""
        for i in strs:
            res += i + "#*"
        return res

    def decode (s):
        res = []
        init = 0
        for i in range(len(s)):
            if(s[i] == '#' and s[i+1] == '*'):
                a = s[init:i]
                res.append(str(a))
                if(i+1 == len(s) -1):
                    break
                init = i+2
        return res
            

strs = ["neet","code","love","you"]


s = Solution.encode(strs=strs)
print(Solution.decode(s))