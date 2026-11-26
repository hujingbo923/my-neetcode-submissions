class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        hang = len(heights)
        lie = len(heights[0])
        pac = [[0 for _ in range(lie)] for _ in range(hang)]
        atl = [[0 for _ in range(lie)] for _ in range(hang)]
        q = deque()
        direct = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(i, j):
            q = deque(i)
            visited = [[False for _ in range(lie)] for _ in range(hang)]
            while q:
                temp = q.popleft()
                for a, b in direct:
                    h1 = temp[0] + a
                    l1 = temp[1] + b
                    if (
                        h1 >= 0
                        and l1 >= 0
                        and h1 < hang
                        and l1 < lie
                        and visited[h1][l1] == False
                        and heights[h1][l1] >= heights[temp[0]][temp[1]]
                    ):
                        j[h1][l1] = 1
                        visited[h1][l1] = True
                        q.append([h1, l1])

        tai = []
        da = []
        for i in range(hang):
            pac[i][0] = 1
            tai.append([i, 0])
            atl[i][lie - 1] = 1
            da.append([i, lie - 1])
        for i in range(lie):
            pac[0][i] = 1
            tai.append([0, i])
            atl[hang - 1][i] = 1
            da.append([hang - 1, i])
        bfs(tai, pac)
        bfs(da, atl)

        ans = []
        for i in range(hang):
            for j in range(lie):
                if pac[i][j] == 1 and atl[i][j] == 1:
                    ans.append([i, j])
        return ans
