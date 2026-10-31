class Solution(object):

  def uniquePaths(self, grid):
    """
        :type grid: List[List[int]]
        :rtype: int
        """
    MOD = 10**9 + 7
    m = len(grid)
    n = len(grid[0])

    
    dp = [[0, 0] for _ in range(n + 1)]

    
    dp[1] = [1, 1]

    for r in range(m):
      for c in range(n):
        if grid[r][c] == 1:
          
          dp[c + 1] = [dp[c + 1][1], dp[c][0]]
        else:
          
          total = (dp[c + 1][1] + dp[c][0]) % MOD
         
          dp[c + 1] = [total, total]

    return dp[n][0]