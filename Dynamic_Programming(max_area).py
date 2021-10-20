#You are given an m x n binary matrix grid.
#An island is a group of 1's (representing land)
#connected 4-directionally (horizontal or vertical.)
#You may assume all four edges of the grid are surrounded by water.

#The area of an island is the number of cells with a value 1 in the island.

#Return the maximum area of an island in grid. If there is no island, return 0.

class Solution(object):
    def maxAreaOfIsland(self, grid):        
        R, C = len(grid), len(grid[0])

        def area(y, x, grid):
            if grid[y][x] == 1:
                ac = 1
                grid[y][x] = 0
            
                if x >= 1 and grid[y][x-1] == 1:
                    ac += area(y, x-1, grid)
                if x+1 < C and grid[y][x+1] == 1:
                    ac += area(y, x+1, grid)
                if y >= 1 and grid[y-1][x] == 1:
                    ac += area(y-1, x, grid)
                if y+1 < R and grid[y+1][x] == 1:
                    ac += area(y+1, x, grid)
            return ac
        amax = 0
        for y in range(R):
            for x in range(C):
                acurr = 0
                if grid[y][x] == 1:
                    acurr = area(y, x, grid)
                    
                    if acurr > amax:
                        amax = acurr
                    
        

        return amax

Example = Solution
grid= [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print("map:")
for _ in range(len(grid)):
    print(grid[_])
print("maximal area = ", Example.maxAreaOfIsland(Example, grid))    

