class Solution(object):
    def maximumSaleItems(self, items, budget):
        """
        :type items: List[List[int]]
        :type budget: int
        :rtype: int
        """
        n = len(items)
        min_price = min(price for _, price in items)
        
        gains = []
        for i in range(n):
            factor_i, _ = items[i]
            free_copies = 0
            for j in range(n):
                if i != j and items[j][0] % factor_i == 0:
                    free_copies += 1
            gains.append(1 + free_copies)
            
        dp = [-1] * (budget + 1)
        dp[0] = 0
        
        for i in range(n):
            price = items[i][1]
            gain = gains[i]
            if price > budget:
                continue
            for c in range(budget, price - 1, -1):
                if dp[c - price] != -1:
                    if dp[c - price] + gain > dp[c]:
                        dp[c] = dp[c - price] + gain
                        
        ans = 0
        for c in range(budget + 1):
            if dp[c] != -1:
                extra_copies = (budget - c) // min_price
                ans = max(ans, dp[c] + extra_copies)
                
        return ans