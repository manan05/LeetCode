class Solution:
    def removeDuplicates(self, s: str) -> str:
        mStack = []
        for i in s:
            if not mStack:
                mStack.append(i)
            else:
                if mStack[-1] == i:
                    mStack.pop()
                else:
                    mStack.append(i)
        return "".join(mStack)
