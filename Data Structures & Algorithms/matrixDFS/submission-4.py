class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        def dfs(grid, r, c, visited):
            rows = len(grid) 
            cols = len(grid[0])

            if (min(r, c) < 0 or c == cols or r == rows or (r,c) in visited or grid[r][c] == 1):
                return 0


            if (r, c) == (rows-1, cols-1):
                return 1


            visited.add((r, c))

            count = 0 
            
            #Going down
            count += dfs(grid, r-1, c, visited)

            #Going up
            count += dfs(grid, r+1, c, visited)

            #Going left
            count += dfs(grid, r, c-1, visited)

            #Going right
            count += dfs(grid, r, c+1, visited)

            visited.remove((r,c))


            return count
            
    

        return dfs(grid, 0, 0, set())