class Solution:
    def solve(self, matrix):
        dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        
        dp[0][0] = matrix[0][0]
        dp[1][0] = matrix[1][0]
        dp[0][1] = matrix[0][1]
        
        for i in range( len(matrix)):
            for j in range( len(matrix[0])):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                dp[i][j] = matrix[i][j] + max(dp[i-1][j], dp[i][j-1])
        return dp[len(dp)-1][len(dp[0])-1]
