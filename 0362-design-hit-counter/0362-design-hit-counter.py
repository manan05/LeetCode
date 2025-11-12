class HitCounter:

    def __init__(self):
        self.res = []

    def hit(self, timestamp: int) -> None:
        self.res.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        i = 0
        while i < len(self.res) and timestamp - self.res[i] >= 300:
            i += 1
        return len(self.res) - i



# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)