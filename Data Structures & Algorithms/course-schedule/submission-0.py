class Solution:
    def canFinish(self, nums: int, pre: List[List[int]]) -> bool:
        hashmap = defaultdict(list)
        for i in range(len(pre)):
            hashmap[pre[i][0]].append(pre[i][1])
        visit = [0] * nums

        def dfs(i):
            if visit[i] == 2:
                return True
            if visit[i] == 1:
                return False
            visit[i] = 1
            for j in hashmap[i]:
                if not dfs(j):
                    return False
            visit[i] = 2
            return True  # 处理不依赖任何课的课程

        for i in range(nums):
            cha = dfs(i)
            if cha == False:
                return False

        return True
