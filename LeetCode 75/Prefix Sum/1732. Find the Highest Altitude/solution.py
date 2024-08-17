

class Solution:
    def highestAltitude(gain):
        ans = [0]
        ans.append(gain[0])
        for i in range(1, len(gain)):
            ans.append(gain[i] + ans[i])
        return max(ans)

gain = [-4,-3,-2,-1,4,3,2]
print(Solution.highestAltitude(gain))
