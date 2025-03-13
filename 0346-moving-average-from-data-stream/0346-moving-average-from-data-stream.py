class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.nums = []

    def next(self, val: int) -> float:
        nums = self.nums
        nums.append(val)
        sumN = sum(nums[-self.size:]) # sum of last (size)
        return sumN/min(self.size, len(nums))


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)