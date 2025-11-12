class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [0] * maxSize
        self.space = maxSize
        self.curr = 0

    def push(self, x: int) -> None:
        if self.space != 0:
            self.stack[self.curr] = x
            self.curr += 1
            self.space -= 1

    def pop(self) -> int:
        if self.curr == 0:
            return -1
        elem = self.stack[self.curr - 1]
        self.curr -= 1
        self.space += 1
        self.stack[self.curr] = 0
        return elem


    def increment(self, k: int, val: int) -> None:
        if k > self.curr - 1:
            for i in range(self.curr):
                self.stack[i] += val
        else:
            for i in range(k):
                self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)