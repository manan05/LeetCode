# numbers is already sorted for us here...


class Solution:
    def twoSum(numbers, target):
        l = 0
        r = len(numbers) - 1

        while l < r:
            val = numbers[l] + numbers[r]
            if val > target:
                r -= 1
            elif val < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []


numbers = [2, 7, 11, 15]
target = 9

print(Solution.twoSum(numbers, target))
