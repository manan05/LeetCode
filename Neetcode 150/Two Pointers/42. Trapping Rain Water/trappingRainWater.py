class Solution:
    def trapRainWaterSol(height):
        size = len(height)
        maxLeft = height.copy()
        maxLeft[0] = 0
        maxRight = height.copy()
        maxRight[size - 1] = 0
        count = 0
        for i in range(1, size):
            maxLeft[i] = max(maxLeft[i - 1], height[i - 1])

        for i in range(size - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i + 1])

        for i in range(size):
            water = min(maxLeft[i], maxRight[i]) - height[i]
            if water >= 0:
                count = count + water
        return count

    def trapRainWaterONSpace(height):
        if not height:
            return 0
        size = len(height)
        l, r = 0, size - 1
        maxL, maxR = height[l], height[r]
        res = 0

        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                res += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR - height[r]
        return res


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Solution.trapRainWaterSol(height))
print(Solution.trapRainWaterONSpace(height=height))
