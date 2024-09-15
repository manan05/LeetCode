class Solution:
    def largestRectangleArea(heights):
        max_area = 0
        stack = [] # idx, height
        
        for i, h in enumerate(heights):
            start = i
            while(stack and stack[-1][1] > h):
                i_dash, h_dash = stack.pop()
                max_area = max(max_area, (h_dash * (i - i_dash)))
                start = i_dash
            stack.append([start, h])

        for i, h in stack:
            max_area = max(max_area, h* (len(heights) - i))

        return max_area

heights = [2,1,5,6,2,3]
print(Solution.largestRectangleArea(heights=heights))
