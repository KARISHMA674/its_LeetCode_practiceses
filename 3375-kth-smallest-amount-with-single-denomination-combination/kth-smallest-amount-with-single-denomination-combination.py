class Solution(object):
    def findKthSmallest(self, coins, k):
        """
        :type coins: List[int]
        :type k: int
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return (a * b) // gcd(a, b)
        
        n = len(coins)
        subsets = []
        
        for mask in range(1, 1 << n):
            current_lcm = 1
            bits = 0
            for i in range(n):
                if (mask >> i) & 1:
                    bits += 1
                    current_lcm = lcm(current_lcm, coins[i])
            
            sign = 1 if bits % 2 == 1 else -1
            subsets.append((current_lcm, sign))
        
        def count(m):
            total = 0
            for lcm_val, sign in subsets:
                total += sign * (m // lcm_val)
            return total

        left = 1
        right = min(coins) * k
        ans = right

        while left <= right:
            mid = (left + right) // 2
            if count(mid) >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
        