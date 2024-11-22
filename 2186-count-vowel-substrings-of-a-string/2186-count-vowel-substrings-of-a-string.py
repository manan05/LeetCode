class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        count = 0

        n = len(word)
        vowels = ['a', 'e', 'i', 'o', 'u']
        for i in range(n-4):
            l = set()
            if(word[i] in vowels):
                l.add(word[i])
                for j in range(i + 1, n):
                    if(word[j] in vowels):
                        l.add(word[j])
                        if(len(l) == 5):
                            count += 1
                    else:
                        break
        return count
