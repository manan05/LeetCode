class HitCounter:

    def __init__(self):
        self.res = deque()

    def hit(self, timestamp: int) -> None:
        self.res.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.res and timestamp - self.res[0] >= 300:
            self.res.popleft()
        return len(self.res)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)