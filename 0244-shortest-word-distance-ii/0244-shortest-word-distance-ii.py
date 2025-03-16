class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.dict_occur = {}
        for i, val in enumerate(wordsDict):
            if val not in self.dict_occur:
                self.dict_occur[val] = [i]
            else:
                self.dict_occur[val].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        minDist = inf
        arrw1 = self.dict_occur[word1]
        arrw2 = self.dict_occur[word2]

        for i in arrw1:
            for j in arrw2:
                minDist = min(minDist, abs(i - j))
        return minDist


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)