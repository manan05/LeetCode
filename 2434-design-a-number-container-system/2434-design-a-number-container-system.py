class NumberContainers:

    def __init__(self):
        self.numToIdx = defaultdict(list)
        self.idxToNum = {}
        

    def change(self, index: int, number: int) -> None:
        self.idxToNum[index] = number

        heapq.heappush(self.numToIdx[number], index)

    def find(self, number: int) -> int:
        if not self.numToIdx[number]:
            return -1
        while self.numToIdx[number]:
            index = self.numToIdx[number][0]

            if self.idxToNum[index] == number:
                return index
            
            heapq.heappop(self.numToIdx[number])

        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)