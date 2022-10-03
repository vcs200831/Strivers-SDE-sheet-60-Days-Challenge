class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        result = 0
        
        stack = [(colors[0], neededTime[0])]
        
        for i in range(1, len(colors)):
            if stack and stack[-1][0] == colors[i]:
                if stack[-1][1] <= neededTime[i]:
                    color, time = stack.pop()
                    result += time
                    stack.append((colors[i], neededTime[i]))
                else:
                    result += neededTime[i]
            else:
                stack.append((colors[i], neededTime[i]))
                
        return result