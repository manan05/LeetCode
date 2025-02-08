class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        res = []
        ball_dict = {}
        color_dict = {}

        for ball, color in queries:
            if ball in ball_dict:
                prev_color = ball_dict[ball]
                color_dict[prev_color] -= 1

                if color_dict[prev_color] == 0:
                    color_dict.pop(prev_color)

            ball_dict[ball] = color

            color_dict[color] = color_dict.get(color, 0) + 1

            res.append(len(color_dict))
        return res