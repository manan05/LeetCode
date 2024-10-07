class Solution:
    def minLength(self, s: str) -> int:
        myStack = []
        if(len(s) == 1):
            return 1
        for i in s:
            if(i == 'B' and myStack):
                if( myStack[-1] == 'A'):
                    myStack.pop()
                    continue
            if(i == 'D' and myStack):
                if (myStack[-1] == 'C'):
                    myStack.pop()
                    continue
            myStack.append(i)
        return len(myStack)
