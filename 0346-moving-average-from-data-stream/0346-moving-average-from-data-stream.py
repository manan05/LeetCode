from collections import deque
class MovingAverage:

    # # Approach 1: Using Array
    # def __init__(self, size: int):
    #     self.size = size
    #     self.nums = []

    # def next(self, val: int) -> float:
    #     # variables for size and nums arr
    #     size = self.size
    #     nums = self.nums
    #     nums.append(val)
    #     sumN = sum(nums[-size:])  # sum of last (size)
    #     return sumN / min(size, len(nums))
    # # Approach 2: Using a Queue
    def __init__(self, size):
        self.size = size
        self.queue = deque()
        self.window_sum = 0

    def next(self, val):
        self.queue.append(val)
        if len(self.queue) > self.size:
            elemPop = self.queue.popleft()
        else:
            elemPop = 0
        self.window_sum = self.window_sum + val - elemPop
        return self.window_sum / min(len(self.queue), self.size)



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)