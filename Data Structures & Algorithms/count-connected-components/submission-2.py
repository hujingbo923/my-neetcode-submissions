class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hashmap = defaultdict(list)
        visited = [False] * n
        for i, j in edges:
            hashmap[i].append(j)
            hashmap[j].append(i)

        def dfs(i):
            visited[i] = True
            for j in hashmap[i]:
                if visited[j] == False:
                    dfs(j)

        cnt = 0
        for i in range(n):
            if visited[i] == False:
                dfs(i)
                cnt += 1
        return cnt
