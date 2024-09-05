class Solution:
    def carFleet(target, position, speed):
        # pair = [[p, s] for p, s in zip(position, speed)]
        
        # stack = []
        # for p,s in sorted(pair)[::-1]: # reverse sorted order
        #     stack.append((target - p)/s)
        #     if(len(stack) >= 2) and stack[-1]<= stack[-2]:
        #         stack.pop()
        # return len(stack)

        pair = []
        stack = []
        for i in range(len(position)):
            pair.append([position[i], speed[i]])
        for p, s in sorted(pair)[::-1]:
            time = target - p
            stack.append(time/ s)
            if(len(stack)>=2 and stack[-1]<= stack[-2]):
                stack.pop()
        return len(stack)




target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

print(Solution.carFleet(target, position, speed=speed))