class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners_map = {}
        losers_map = {}

        for win, loss in matches:
            if win in winners_map:
                winners_map[win] += 1
            else:
                winners_map[win] = 1

            if loss not in losers_map:
                losers_map[loss] = 1
            else:
                losers_map[loss] += 1
        
        noLoss = []
        oneLoss = []

        for i in winners_map.keys():
            if i not in losers_map:
                noLoss.append(i)
        
        for i, j in losers_map.items():
            if j == 1:
                oneLoss.append(i)
        noLoss.sort()
        oneLoss.sort()
        return [noLoss, oneLoss]