class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        direct = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        hang = len(grid)
        lie = len(grid[0])
        time = 0

        def bfs():
            nonlocal time
            if not q:
                return time
            while q:
                lenth = len(q)
                hasnew = False
                for t in range(lenth):
                    temp = q.popleft()
                    for i, j in direct:
                        h = i + temp[0]
                        l = j + temp[1]
                        if h >= 0 and h < hang and l >= 0 and l < lie and grid[h][l] == 1:
                            grid[h][l] = 2
                            hasnew = True #必须感染新的才能加一，要不然不算时间
                            q.append([h, l])
                if hasnew == True:
                    time += 1

        for i in range(hang):
            for j in range(lie):
                if grid[i][j] == 2:
                    q.append([i, j])
        bfs()
        for i in range(hang):
            for j in range(lie):
                if grid[i][j] == 1:
                    return -1
        return time
