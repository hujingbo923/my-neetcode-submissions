class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        decide = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def bfs(hang, lie):
            q = deque()
            visited[hang][lie] = True
            q.append([hang, lie])
            while q:
                temp = q.popleft()
                for i, j in decide:
                    hang1, lie1 = temp[0] + i, temp[1] + j
                    if (
                        hang1 < len(grid)
                        and lie1 < len(grid[0])
                        and hang1 >= 0
                        and lie1 >= 0
                        and grid[hang1][lie1] == "1"
                        and visited[hang1][lie1] == False
                    ):
                        q.append([hang1, lie1])
                        visited[hang1][lie1] = True

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and visited[i][j] == False:
                    bfs(i, j)
                    cnt += 1
        return cnt
