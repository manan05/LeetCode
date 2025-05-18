class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = [i[0] for i in intervals]
        ends = [i[1] for i in intervals]
        starts.sort()
        ends.sort()
        rooms, curr = 1, 1
        i, j = 1, 0
        while i < len(intervals) and j < len(intervals):
            if starts[i] < ends[j]:
                curr += 1
                i += 1
            else:
                curr -= 1
                j += 1
            rooms = max(rooms, curr)
        return rooms
