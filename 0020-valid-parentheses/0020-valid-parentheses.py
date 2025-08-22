class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mDict = {'}': '{', ']': '[', ')': '('}
        for i in s:
            if i not in mDict:
                stack.append(i)
            else:
                if stack and stack[-1] == mDict[i]:
                    stack.pop(-1)
                else:
                    return False
        return True if len(stack) == 0 else False
