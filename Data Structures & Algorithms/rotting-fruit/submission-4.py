from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        rotten = set()
        queue = deque()


        fresh_count = 0


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col))
                    rotten.add((row, col))
                elif grid[row][col] == 1:
                    fresh_count += 1
        

        minutes = 0


        while queue:
            made_progress = False

            for _ in range(len(queue)):
                r, c = queue.popleft()


            
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    new_row = r + dr
                    new_col = c + dc
                    if (min(new_row, new_col) < 0) or (new_row == rows) or (new_col == cols) or ((new_row, new_col) in rotten) or grid[new_row][new_col] == 0:
                        continue
                    
                    queue.append((new_row, new_col))
                    rotten.add((new_row, new_col))
                    fresh_count -= 1
                    made_progress = True


            if made_progress:
                minutes += 1
            
            
            

        return minutes if fresh_count == 0 else -1





