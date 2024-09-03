class Solution:
    def evalRPN(tokens):
        stack = []
        for i in tokens:
            if i == "+" or i == "-" or i == "/" or i == "*":
                # pop 2 elements on top and push it on top of stack
                num1 = stack.pop(-1)
                num2 = stack.pop(-1)
                if i == "+":
                    val = num1 + num2
                elif i == "-":
                    val = num2 - num1
                elif i == "/":
                    val = int(num2 / num1)
                elif i == "*":
                    val = num1 * num2
                stack.append(val)
            else:
                stack.append(int(i))
        return stack.pop()


tokens = ["2", "1", "+", "3", "*"]
tokens2 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

print(Solution.evalRPN(tokens=tokens))
print(Solution.evalRPN(tokens=tokens2))
