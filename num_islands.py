from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == None or len(grid) == 0:
            return 0
        num_rows = len(grid)
        num_cols = len(grid[0])
        num_islands = 0
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == "1":
                    num_islands += 1
                    self._dfs(grid, row, col, num_rows, num_cols)
        return num_islands
            
            
    def _dfs(self, grid, row, col, num_rows, num_cols):
        if row < 0 or col < 0 or row >= num_rows or col >= num_cols or grid[row][col] == "0":
            return
        grid[row][col] = "0"
        self._dfs(grid, row - 1, col, num_rows, num_cols)
        self._dfs(grid, row + 1, col, num_rows, num_cols)
        self._dfs(grid, row, col - 1, num_rows, num_cols)
        self._dfs(grid, row, col + 1, num_rows, num_cols)

sol = Solution()
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(sol.numIslands(grid)) # 3
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(sol.numIslands(grid)) # 1

grid = [["1","1","1"],
        ["0","1","0"],
        ["1","1","1"]]
print(sol.numIslands(grid)) # 1
grid = [["1","0","1","1","1"],
        ["1","0","1","0","1"],
        ["1","1","1","0","1"]]
print(sol.numIslands(grid)) # 1

    # def _searchV(self, grid: List[List[str]], curr_row, curr_col, val, numRows: int) -> int:
    #     for row in range(curr_row, numRows):
    #         if grid[row][curr_col] == val:
    #             return (row, curr_col)
    #     return None
    # def _searchH(self, grid: List[List[str]], curr_row, curr_col, val, numCols: int) -> int:
    #     for col in range(curr_col, numCols):
    #         if grid[curr_row][col] == val:
    #             return (curr_row, col)
    #     return None