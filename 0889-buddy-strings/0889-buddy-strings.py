class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        # if both of them are same
        if s == goal:
            temp = set(s)
            return True if len(temp) < len(s) else False

        pairs = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                pairs.append((s[i], goal[i]))
        if len(pairs) != 2:
            return False

        p1 = pairs[0]
        p2 = pairs[1]
        return True if (p1[0] == p2[1] and p1[1] == p2[0]) else False
