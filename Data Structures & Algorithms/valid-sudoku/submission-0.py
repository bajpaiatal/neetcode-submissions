class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colVis = [set() for _ in range(9)]
        rowVis = [set() for _ in range(9)]
        boxVis = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    bx = 3*(i//3) + (j//3)
                    if (board[i][j] in rowVis[i] 
                    or board[i][j] in colVis[j] 
                    or board[i][j] in boxVis[bx]):
                        return False
                    rowVis[i].add(board[i][j])
                    colVis[j].add(board[i][j])
                    boxVis[bx].add(board[i][j])
        return True
