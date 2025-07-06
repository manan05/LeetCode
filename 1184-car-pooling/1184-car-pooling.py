class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        times = []
        for trip in trips:
            times.append([trip[1], trip[0]])
            times.append([trip[2], -trip[0]])
        used_capacity = 0
        times.sort()
        for time, passenger in times:
            used_capacity += passenger
            if used_capacity > capacity:
                return False
        return True
