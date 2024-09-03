class Solution:
    def isValid(s):
        myStack = []
        for i in s:
            # check if opening bracket
            if(i == '(' or i == '[' or i == '{'):
                myStack.append(i)
            else:
                if not myStack:
                    return False
                elif(i == ')' and myStack[-1] == '(' or i == '}' and myStack[-1] == '{' or i == ']' and myStack[-1] == '['):
                    myStack.pop()
                else:
                    return False
        if(myStack):
            return False
        else:
            return True

s = "()[]{}"
s2 = "(]"
s3 = "(])"

print(Solution.isValid(s3))