from collections import Counter

class Solution(object):
    def smallestUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        MOD1, MOD2 = 10**9 + 7, 10**9 + 9
        BASE1, BASE2 = 1315423911, 2654435761

        def has_unique_subarray(length):
            # Compute BASE^(length - 1) % MOD
            pow1 = pow(BASE1, length - 1, MOD1)
            pow2 = pow(BASE2, length - 1, MOD2)

            h1 = h2 = 0
            for i in range(length):
                # Offset elements to handle negative numbers or zeros safely
                val = nums[i] + 1000000001
                h1 = (h1 * BASE1 + val) % MOD1
                h2 = (h2 * BASE2 + val) % MOD2

            seen = {(h1, h2): 1}

            for i in range(length, n):
                out_val = nums[i - length] + 1000000001
                in_val = nums[i] + 1000000001

                h1 = ((h1 - out_val * pow1) * BASE1 + in_val) % MOD1
                h2 = ((h2 - out_val * pow2) * BASE2 + in_val) % MOD2

                pair = (h1, h2)
                seen[pair] = seen.get(pair, 0) + 1

            return any(count == 1 for count in seen.values())

        left, right = 1, n
        ans = n

        while left <= right:
            mid = (left + right) // 2
            if has_unique_subarray(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans