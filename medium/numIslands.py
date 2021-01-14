class Solution:
    def solve(self, matrix):
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    self.bfs(matrix, i, j)
                    count += 1
        return count
    
    def bfs(self, matrix, row, col):
        if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or matrix[row][col] == 0:
            return
        
        #use these two to check nbh
        rows = [-1, 0, 0, 1]
        cols = [0, -1, 1, 0]
        matrix[row][col] = 0
        
        for ind in range(4):
            self.bfs(matrix, row + rows[ind], col + cols[ind])
