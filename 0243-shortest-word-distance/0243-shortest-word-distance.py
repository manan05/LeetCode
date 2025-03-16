class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # # Brute Force: 
        # minDist = len(wordsDict)
        # for i in range(len(wordsDict)):
        #     if wordsDict[i] == word1:
        #         for j in range(len(wordsDict)):
        #             if wordsDict[j] == word2:
        #                 minDist = min(minDist, abs(i - j))

        # return minDist
        
        # # Optimized: OnePass
        idx_word1 = -1
        idx_word2 = -1
        minDist = len(wordsDict)
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                idx_word1 = i
            elif wordsDict[i] == word2:
                idx_word2 = i
            
            if idx_word1 != -1 and idx_word2 != -1:
                minDist = min(minDist, abs(idx_word1 - idx_word2))
        return minDist
