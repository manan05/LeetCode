class Solution:
    def generateParenthesis(n):
        # only add open parentheses if open < n
        # only add closing parentheses if close < open
        # valid parenteheses if open == closed == n

        stack = []
        res = []
        def backtrack(openC, closeC):
            # base case
            if(openC == closeC == n):
                res.append("".join(stack))
                return

            if(openC < n):
                stack.append("(")
                backtrack(openC +1, closeC)
                stack.pop()

            if (closeC < openC):
                stack.append(")")
                backtrack(openC, closeC + 1)
                stack.pop()

        backtrack(0, 0)
        return res

n = 2
print(Solution.generateParenthesis(n))