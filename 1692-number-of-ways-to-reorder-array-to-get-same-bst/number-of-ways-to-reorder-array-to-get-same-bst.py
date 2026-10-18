import math

class Solution(object):
    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7

        def nCr(n, r):
            return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

        def count_ways(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            comb = nCr(len(left) + len(right), len(left))
            
            return (comb * count_ways(left) * count_ways(right)) % MOD

        return (count_ways(nums) - 1) % MOD