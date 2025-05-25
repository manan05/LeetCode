class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()

        def helper(index, curr, currSum):
            # base case
            if currSum == target:
                res.append(curr[:])
                return
            if index == n or currSum > target:
                return

            # include
            currSum += candidates[index]
            curr.append(candidates[index])
            helper(index, curr, currSum)

            # exclude
            currSum -= candidates[index]
            curr.pop()
            helper(index + 1, curr, currSum)

        helper(0, [], 0)
        return res
