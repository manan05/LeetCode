class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        myStack = []
        for i in s:
            if(i =='('):
                myStack.append(i)
            elif(i == ')' and myStack):
                if(myStack[-1] == '('):
                    myStack.pop()
                else:
                    myStack.append(i)
            else:
                myStack.append(i)
        return len(myStack)