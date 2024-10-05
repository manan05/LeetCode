class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        l = 0
        r = k
        count = 0
        numStr = str(num)
        subNum = int(numStr[l:r])
        print(subNum)
        if (num % subNum == 0):
            count += 1
        l += 1
        r += 1
        while (r <= len(numStr)):
            ss = int(numStr[l:r])
            if (ss != 0):
                if (num % ss == 0):
                    print("here")
                    count += 1
            r += 1
            l += 1
        return count
