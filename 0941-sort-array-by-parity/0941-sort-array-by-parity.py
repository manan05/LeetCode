class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        oddA = []
        evenA = []
        for i in nums:
            if i%2 == 0:
                evenA.append(i)
            else:
                oddA.append(i)
        return evenA + oddA