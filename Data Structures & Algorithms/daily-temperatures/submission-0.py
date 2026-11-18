class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack =[]
        ans = [0]*len(temperatures)
        for i in range(len(temperatures)):
            if not stack:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]]<temperatures[i]:
                    tmp = stack.pop()
                    ans[tmp] = i-tmp
                stack.append(i)
                #tmp = stack.pop()
                #if temperatures[tmp] < temperatures[i]:
                #    ans[tmp]=i-tmp
                #    stack.append(i)
                #如果用if的话，出现71 69 72的时候，弹出69就继续下一个循环了，但实际上71也需要
        return ans