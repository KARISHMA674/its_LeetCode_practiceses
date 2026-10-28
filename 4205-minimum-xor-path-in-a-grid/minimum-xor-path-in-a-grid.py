class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        dp = [set() for _ in range(n)]
        dp[0].add(grid[0][0])
        
        for c in range(1, n):
            val = grid[0][c]
            dp[c] = {x ^ val for x in dp[c - 1]}
        
        for r in range(1, m):
            val = grid[r][0]
            dp[0] = {x ^ val for x in dp[0]}
            
            for c in range(1, n):
                val = grid[r][c]
                combined_prev = dp[c] | dp[c - 1]
                dp[c] = {x ^ val for x in combined_prev}
                
        return min(dp[-1])