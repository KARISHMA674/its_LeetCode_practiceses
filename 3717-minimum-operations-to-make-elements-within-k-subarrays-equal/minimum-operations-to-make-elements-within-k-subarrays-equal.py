from bisect import bisect_left
from sortedcontainers import SortedList

class Solution(object):
    def minOperations(self, nums, x, k):
        """
        :type nums: List[int]
        :type x: int
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if x == 1:
            return 0
        
        sl = SortedList()
        lower_count = (x + 1) // 2
        lower_sum = [0]
        cost = [0] * (n - x + 1)

        def add_val(val):
            idx = sl.bisect_left(val)
            sl.add(val)
            if idx < lower_count:
                lower_sum[0] += val
                if len(sl) > lower_count:
                    lower_sum[0] -= sl[lower_count]

        def remove_val(val):
            idx = sl.bisect_left(val)
            sl.remove(val)
            if idx < lower_count:
                lower_sum[0] -= val
                if len(sl) >= lower_count:
                    lower_sum[0] += sl[lower_count - 1]

        total_sum = 0
        for i in range(x):
            add_val(nums[i])
            total_sum += nums[i]
        
        median = sl[lower_count - 1]
        upper_sum = total_sum - lower_sum[0]
        upper_count = x - lower_count
        cost[0] = (median * lower_count - lower_sum[0]) + (upper_sum - median * upper_count)

        for i in range(1, n - x + 1):
            remove_val(nums[i - 1])
            add_val(nums[i + x - 1])
            total_sum += nums[i + x - 1] - nums[i - 1]
            
            median = sl[lower_count - 1]
            upper_sum = total_sum - lower_sum[0]
            cost[i] = (median * lower_count - lower_sum[0]) + (upper_sum - median * upper_count)

        dp = [0] * (n + 1)
        for c in range(1, k + 1):
            next_dp = [float('inf')] * (n + 1)
            for i in range(n - c * x, -1, -1):
                skip = next_dp[i + 1]
                pick = cost[i] + dp[i + x]
                next_dp[i] = skip if skip < pick else pick
            dp = next_dp

        return dp[0]