class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        shortest_distance = float('inf')
        prev_index = -1

        for i, word in enumerate(wordsDict):
            if word == word1 or word == word2:
                if prev_index != -1 and (wordsDict[prev_index] != word or word1 == word2):
                    shortest_distance = min(shortest_distance, i - prev_index)
                prev_index = i

        return shortest_distance