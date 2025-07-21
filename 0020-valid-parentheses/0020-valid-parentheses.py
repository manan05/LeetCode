class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mDict = {')': '(', ']':'[', '}':'{'}
        for char in s:
            if char in mDict:
                top = stack.pop() if stack else '#'
                if mDict[char] != top:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
