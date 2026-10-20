class Solution(object):
    def sortableIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return 1

        
        pref_max = [0] * n
        pref_max[0] = nums[0]
        for i in range(1, n):
            pref_max[i] = max(pref_max[i - 1], nums[i])

        suff_min = [0] * n
        suff_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suff_min[i] = min(suff_min[i + 1], nums[i])

        
        pref_drops = [0] * n
        for i in range(n - 1):
            pref_drops[i + 1] = pref_drops[i] + (1 if nums[i] > nums[i + 1] else 0)

        total_sum = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            is_sortable = True

            
            for boundary in range(k, n, k):
                if pref_max[boundary - 1] > suff_min[boundary]:
                    is_sortable = False
                    break

            if not is_sortable:
                continue

            
            if k > 1:
                for start in range(0, n, k):
                    end = start + k - 1
                    
                    internal_drops = pref_drops[end] - pref_drops[start]
                    
                    wrap_drop = 1 if nums[end] > nums[start] else 0

                    if internal_drops + wrap_drop > 1:
                        is_sortable = False
                        break

            if is_sortable:
                total_sum += k

        return total_sum