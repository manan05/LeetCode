# QuestionLink:  https://leetcode.com/problems/string-compression/description/?envType=study-plan-v2&envId=leetcode-75

# Companies: Expedia ✯   Amazon ✯   Microsoft ✯   Goldman Sachs ✯   Apple ✯   Facebook   Visa   Yandex   Redfin

class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        s+= chars[0]
        i = 1
        count = 1
        while(count< len(chars)):
            if(chars[count-1] == chars[count]):
                i +=1
                count +=1
            else:
                if(i != 1):
                    s += str(i)
                    i = 1
                    s += chars[count]
                    count +=1
                else:
                    s += chars[count]
                    count +=1
        if(i != 1):
            s += str(i)
        for j in range(len(s)):
            chars[j] = s[j] 
        return len(s)