class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dt = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != '.':
                    r = ('r', i, board[i][j])
                    c = ('c', j, board[i][j])
                    sq = ('sq', i//3, j//3, board[i][j])
                    if (r in dt) or (c in dt) or (sq in dt):
                        return False
                    else:
                        dt.add(r)
                        dt.add(c)
                        dt.add(sq)
        return True
