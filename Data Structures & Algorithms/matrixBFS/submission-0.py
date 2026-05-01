from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        visited = set()

        queue.append((0, 0))
        visited.add((0, 0))


        length = 0

        while queue:
            for i in range(len(queue)):

                r, c = queue.popleft()

                if r == rows - 1 and c == cols -1:
                    return length


                directions = [[-1, 0], [1, 0], [0,1], [0, -1]]

                for dr, dc in directions:
                    new_row = r + dr
                    new_col = c + dc

                    if (min(new_row, new_col) < 0) or (new_row == rows) or (new_col == cols) or (grid[new_row][new_col] == 1) or ((new_row, new_col) in visited):
                        continue
                    
                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col))

            length += 1
        
        return -1







                    
                     