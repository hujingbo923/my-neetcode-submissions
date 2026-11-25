class Solution:
    def solve(self, board: List[List[str]]) -> None:
        hang = len(board)
        lie = len(board[0])

        def dfs(h, l):
            if h < 0 or l < 0 or h >= hang or l >= lie or board[h][l] == "X" or board[h][l] == "V":
                return
            else:
                board[h][l] = "V"
            if h + 1 < hang:
                dfs(h + 1, l)
            if h - 1 >= 0:
                dfs(h - 1, l)
            if l + 1 < lie:
                dfs(h, l + 1)
            if l - 1 >= 0:
                dfs(h, l - 1)

        for i in range(hang):
            for j in range(2):
                if j == 0:
                    dfs(i, 0)
                else:
                    dfs(i, lie - 1)
        for i in range(lie):
            for j in range(2):
                if j == 0:
                    dfs(0, i)
                else:
                    dfs(hang - 1, i)
        for i in range(hang):
            for j in range(lie):
                if board[i][j] == "O":
                    board[i][j] = "X"
        for i in range(hang):
            for j in range(lie):
                if board[i][j] == "V":
                    board[i][j] = "O"
        return
