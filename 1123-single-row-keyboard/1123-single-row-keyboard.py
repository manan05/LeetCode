class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        kb_dict = {}
        s = 0
        for i in range(26):
            kb_dict[keyboard[i]] = i
        s = abs(kb_dict.get(word[0]) - 0)
        for i in range(1, len(word)):
            diff = abs(kb_dict.get(word[i]) - kb_dict.get(word[i-1]))
            s += diff
        return s