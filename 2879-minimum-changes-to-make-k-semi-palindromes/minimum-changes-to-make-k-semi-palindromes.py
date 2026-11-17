class Solution(object):
    def minimumChanges(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        
       
        divisors = [[] for _ in range(n + 1)]
        for L in range(2, n + 1):
            for d in range(1, L // 2 + 1):
                if L % d == 0:
                    divisors[L].append(d)
         
        def get_cost(i, j):
            L = j - i
            min_changes = float('inf')
            for d in divisors[L]:
                changes = 0
                
                for rem in range(d):
                    left = i + rem
                    right = j - d + rem
                    while left < right:
                        if s[left] != s[right]:
                            changes += 1
                        left += d
                        right -= d
                if changes < min_changes:
                    min_changes = changes
            return min_changes

        
        cost = [[float('inf')] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(i + 2, n + 1):  
                cost[i][j] = get_cost(i, j)
                
        
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        
        for p in range(1, k + 1):
            
            for j in range(2 * p, n + 1):
                
                for i in range(2 * (p - 1), j - 1):
                    if dp[i][p - 1] != float('inf'):
                        dp[j][p] = min(dp[j][p], dp[i][p - 1] + cost[i][j])
                        
        return dp[n][k]