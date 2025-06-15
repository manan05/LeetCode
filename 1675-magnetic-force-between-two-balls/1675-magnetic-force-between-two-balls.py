class Solution:
    def canPlace(self, position: List[int], m: int, dist: int) -> bool:
        currC = 1
        lastPlaced = position[0]
        for i in range(1, len(position)):
            if position[i] - lastPlaced >= dist:
                currC += 1
                lastPlaced = position[i]
            if currC >= m:
                return True
        return False

    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()
        low = 1
        high = position[n - 1] - position[0]
        while low <= high:
            mid = (low + high) // 2
            if self.canPlace(position, m, mid):
                low = mid + 1
            else:
                high = mid - 1
        return high
