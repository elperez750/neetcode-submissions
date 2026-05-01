class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
            ROWS, COLS = len(board), len(board[0])
            potential = set([])

            def dfs(potential, r, c, position):
                print(r, c)
                if position == len(word):
                    return True

                if (min(r, c) < 0) or ((r, c) in potential) or (r == ROWS) or (c == COLS):
                    return False

                
                if board[r][c] == word[position]:
                    potential.add((r, c))
                    position += 1
                    print(potential)
                    print(position)
                    if dfs(potential, r-1, c, position) or dfs(potential, r+1, c, position) or dfs(potential, r, c-1, position ) or dfs(potential, r, c+1, position):
                        return True
                
                    potential.remove((r, c))


            for r in range(ROWS):
                for c in range(COLS):
                    if dfs(potential, r, c, 0):
                        return True
            return False
