from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCounter = Counter(ransomNote)
        magazineCounter = Counter(magazine)
        for item in ransomCounter.items():
            if item[0] not in magazineCounter:
                return False
            else:
                if item[1] > magazineCounter.get(item[0], 0):
                    return False
        return True
