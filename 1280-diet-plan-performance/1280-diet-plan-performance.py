class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        n = len(calories)
        l = 0
        r = k
        points = 0
        sumArr = sum(calories[l:r])
        if(sumArr > upper):
            points += 1
        if (sumArr < lower):
            points -= 1
        for r in range(k, n):
            sumArr = sumArr + calories[r] - calories[l]
            if(sumArr > upper):
                points += 1
            if(sumArr < lower):
                points -= 1
            l += 1
        return points