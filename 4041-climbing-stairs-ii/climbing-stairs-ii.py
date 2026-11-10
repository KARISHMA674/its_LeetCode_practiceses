class Solution(object):
    def climbStairs(self, n, costs):
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            step_cost = costs[i - 1]
            for j in range(max(0, i - 3), i):
                jump_len = i - j
                cost = dp[j] + step_cost + jump_len * jump_len
                if cost < dp[i]:
                    dp[i] = cost
                    
        return dp[n]