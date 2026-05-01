from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i: set() for i in range(9)}
        cols = {i: set() for i in range(9)}
        subbox = {(i, j): set() for i in range(3) for j in range(3)}

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = board[i][j]

                    if num in rows[i] or num in cols[j] or num in subbox[(i // 3, j // 3)]:
                        return False  # Duplicate found

                    rows[i].add(num)
                    cols[j].add(num)
                    subbox[(i // 3, j // 3)].add(num)

        return True
