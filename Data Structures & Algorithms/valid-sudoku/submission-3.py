class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        subbox = {}


        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    rows.setdefault(i, []).append(board[i][j])
                    cols.setdefault(j, []).append(board[i][j])
                    subbox.setdefault((i // 3 , j // 3), []).append(board[i][j])

       
        for key, sublist in rows.items():
            if len(sublist) != len(set(sublist)):
                return False

        for key, sublist in cols.items():
            if len(sublist) != len(set(sublist)):
                return False

        for key, sublist in subbox.items():
             if len(sublist) != len(set(sublist)):
                return False

        return True     

        
       
