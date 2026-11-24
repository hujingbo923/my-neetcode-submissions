class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0

        def dfs(hang, lie):
            if (
                hang >= len(grid)
                or lie >= len(grid[0])
                or hang < 0
                or lie < 0
                or grid[hang][lie] == "0"
            ):
                return
            if grid[hang][lie] == "1":
                grid[hang][lie] = "0"
            dfs(hang + 1, lie)
            dfs(hang - 1, lie)
            dfs(hang, lie + 1)
            dfs(hang, lie - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    cnt += 1
        return cnt
