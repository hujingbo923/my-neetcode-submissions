class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash = set()
        for i in range(9):
            hash = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in hash:
                        return False
                    hash.add(board[i][j])
        for j in range(9):
            hash = set()
            for i in range(9):
                if board[i][j] != '.':
                    if board[i][j] in hash:
                        return False
                    hash.add(board[i][j])
        for i in range(0, 9, 3):
            for j in range(0 ,9, 3):
                hash = set()
                for i1 in range(i, i+3):
                    for j1 in range(j, j+3):
                        if board[i1][j1] != '.':
                            if board[i1][j1] in hash:
                                return False
                        hash.add(board[i1][j1])
        return True


