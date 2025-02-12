class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # iteration
        # while part in s:
        #     start = s.find(part)
        #     s = s[:start] + s[start + len(part):]
        # return s

        # using Stack
        myStack = []
        len_part = len(part)

        for ch in s:
            myStack.append(ch)

            if (len(myStack) >= len_part and ("".join(myStack[-len_part:]) == part)):
                for _ in range(len_part):
                    myStack.pop()

        return "".join(myStack)