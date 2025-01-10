class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        moves = []
        for i in range(len(boxes)):
            l = 0
            for j in range(0, len(boxes)):
                if boxes[j] == '1' and j != i:
                    l += abs(i - j)
            moves.append(l)
        return moves