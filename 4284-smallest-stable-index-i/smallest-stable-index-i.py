class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        n=len(nums)
        if n==0:
            return -1

        suf_min=[0] * n
        suf_min[-1] = nums[-1]
        for i in range (n-2,-1,-1):
            suf_min[i] = min(nums[i],suf_min[i+1])

        pref_max=nums[0]
        for i in range(n):
            if nums[i]>pref_max:
                pref_max=nums[i]
            if pref_max-suf_min[i] <=k:
                return i
        return -1                    