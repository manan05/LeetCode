class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if(self.minStack):
            self.minStack.append(min(val, self.minStack[-1]))
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(10)
obj.push(20)
obj.pop()
param_3 = obj.top()
print(param_3)
param_4 = obj.getMin()