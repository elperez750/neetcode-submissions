
class Solution {


    public void markIslands(char[][] grid, ArrayList<String> visited, int i, int j, int xUpperBound, int yUpperBound) {
        if (i < 0 || i == xUpperBound) {
            return;
        }

        if (j < 0 || j == yUpperBound) {
            return;
        }

        if (grid[i][j] == '0') {
            return;
        }


        if(visited.contains(String.valueOf(i) + String.valueOf(j))){
            return;

        }

        visited.add(String.valueOf(i) + String.valueOf(j));


          // Going down
        markIslands(grid, visited, i + 1, j, xUpperBound, yUpperBound);

            // Going up
        markIslands(grid, visited, i - 1, j, xUpperBound, yUpperBound);

            // Going left
        markIslands(grid, visited, i, j - 1, xUpperBound, yUpperBound);

            // Going right
        markIslands(grid, visited, i, j + 1, xUpperBound, yUpperBound);

    }


    public int numIslands(char[][] grid) {
        ArrayList<String> visited = new ArrayList<>();
        int islandCount = 0;

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == '1' && !visited.contains(String.valueOf(i) + String.valueOf(j))){
                      
                    markIslands(grid, visited, i, j, grid.length, grid[i].length);
                    islandCount += 1;
                 
                  
                }
            }
        }


        return islandCount;
    }



  
}
