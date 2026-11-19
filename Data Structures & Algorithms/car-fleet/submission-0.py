class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position:
            return 0
        time = []
        ans = 1
        for i in range(len(position)):
            time.append((target - position[i])/speed[i])
        pairs = sorted(zip(position, time), reverse=True)
        time = [y for x, y in pairs]
        stack = []
        stack.append(time[0])
        for i in range(1, len(time)):
            if stack and stack[-1] >= time[i]:
                continue
            if stack and stack[-1] < time[i]:
                stack.append(time[i])
                ans+=1
        return ans
# 根据第一个列表的顺序排列，用zip，默认升序，降序加reverse
# 直接看到达目的地的时间，如果后面时间短于前面车队，就说明能追上
# 比如time 132，3追不上1，所以3入，但是2能追上3，所以2不入（合并进3了）
