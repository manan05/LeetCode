class Solution:
    def dailyTemperaturesON2(temps):
        # this is a O(N2) solution that passes 36/48 test cases
        minStack = [0 for x in temps]
        
        for i in range(len(temps)):
            for j in range(i+1, len(temps)):
                if(temps[j] > temps[i]):
                    minStack[i] = j - i
                    break
        return minStack
    
    def dailyTemperatures(temps):
        l = len(temps)
        stack = [] # pair [temp, index]
        res = [0] * l
        for i in range(l) :
            while stack and temps[stack[-1]] < temps[i]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res
            




temps = [73,74,75,71,69,72,76,73]
print(Solution.dailyTemperatures(temps))