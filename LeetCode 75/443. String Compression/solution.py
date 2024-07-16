class Solution:
    # Using Hashmap or dict but we cannot (31/76) pass
    def compress(chars):
        hashmap = {}
        for i in range(len(chars)):
            if(chars[i] not in hashmap.keys()):
               hashmap[chars[i]] = 1
            else:
                z = hashmap.get(chars[i]) + 1
                hashmap[chars[i]] = z
        s = ""
        for i,j in hashmap.items():
            s += i
            if(j == 1):
                pass
            else:
                s += str(j)
        for i in range(len(s)):
            chars[i] = s[i]
        
        return len(s)          

chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

print(Solution.compress(chars))