from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = [0]*row*col
        size = 0
        for i in range(row):
            for j in range(col):
                (visited, current_size) = self.check_island(grid, visited, i, j ,0)
                size = max(current_size, size)
        return size

    def check_island(self,  grid: List[List[int]], visited, sr,sc,size):
        if (0<=sr<len(grid) and 0<=sc<len(grid[0])):
            print(sr)
            print(sc)
            print(sr*len(grid)+sc)
            print(visited[sr*len(grid[0])+sc])
            if grid[sr][sc] == 1 and visited[sr*len(grid[0])+sc] == 0:
                size+=1
                visited[sr*len(grid[0]) + sc] = 1
                (visited, size) = self.check_island(grid,visited,sr-1,sc,size)
                (visited, size) = self.check_island(grid,visited,sr+1,sc,size)
                (visited, size) = self.check_island(grid,visited,sr,sc-1,size)
                (visited, size) = self.check_island(grid,visited,sr,sc+1,size)


        return (visited,size)

a= Solution()
print(a.maxAreaOfIsland([[0],[1]]))
