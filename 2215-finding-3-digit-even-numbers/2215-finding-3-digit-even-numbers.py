class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        hashset = set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    num = 100*digits[i] + 10*digits[j] + digits[k]
                    if i == j or j == k or i == k:
                        continue
                    if num not in hashset:
                        if num % 2 == 0 and num >= 100:
                            hashset.add(num)
        return sorted(list(hashset))
