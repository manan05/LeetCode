class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Approach 1: Input Array Sorted: Binary Search
        left, right = 0, len(numbers) - 1
        while left < right:
            mySum = numbers[left] + numbers[right]
            if mySum == target:
                return [left + 1, right + 1]
            elif mySum > target:
                right -= 1
            else:
                left += 1
