class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for i in words:
            z = set(i)
            for char in z:
                if(char not in allowed):
                    count += 1
                    break
        return len(words) - count
    
allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]

print(Solution.countConsistentStrings(allowed, words))